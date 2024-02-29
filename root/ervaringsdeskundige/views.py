from .forms import RegisterForm
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from ervaringsdeskundige.models import User
from .forms import RegisterForm, ToezichthoudersForm
from main.models import (
    Onderzoeken,
    Deelnames,
    Beperkingen,
    BeperkingenErvaringsdeskundigen,
)


def register(request):
    limitations = Beperkingen.objects.all()
    if request.method == "POST":
        form = RegisterForm(request.POST)
        supervisors_post = ToezichthoudersForm(request.POST)

        if form.is_valid():
            user = form.save()

            selected_limitations = request.POST.getlist("selected_limitations")
            user_id = user.id

            for selected_limitation in selected_limitations:
                ervaringsdeskundige_beperking = BeperkingenErvaringsdeskundigen(
                    beperking_id=int(selected_limitation),
                    ervaringsdeskundigen_id=user_id,
                )
                ervaringsdeskundige_beperking.save()

            if supervisors_post.is_valid():
                toezichthouder = supervisors_post.save(commit=False)
                toezichthouder.ervaringsdeskundige = user_id
                toezichthouder.save()

            return redirect("/")
    else:
        form = RegisterForm()
        supervisors = ToezichthoudersForm()

    return render(
        request,
        "ervaringsdeskundige/register.html",
        {"form": form, "limitations": limitations, "supervisors": supervisors},
    )


@login_required()
def dashboard_ervaringsdeskundige(request):
    current_user = request.user
    return render(request, "ervaringsdeskundige/dashboard.html", {"user": current_user})


@login_required
def edit_profile(request):
    current_user = request.user
    if request.method == "POST":
        form = RegisterForm(request.POST, instance=current_user)
        if form.is_valid():
            form.save()
            return redirect("/ervaringsdeskundige/dashboard")
    else:
        form = RegisterForm(instance=current_user)

    return render(request, "ervaringsdeskundige/edit_profile.html", {"form": form})


def logout_ervaringsdeskundige(request):
    logout(request)
    return redirect("/login")


@login_required
def onderzoeken(request):
    investigations = Onderzoeken.objects.all()
    return render(
        request,
        "ervaringsdeskundige/onderzoeken.html",
        {"investigations": investigations},
    )


@login_required
def register_investigation(request, investigation_id):
    user_id = request.user.id

    new_register_investigation = Deelnames(
        ervaringsdeskundige_id=user_id, onderzoeks_id=investigation_id, status=2
    )
    new_register_investigation.save()

    return redirect("/ervaringsdeskundige/register_investigation_succes")


@login_required
def register_investigation_succes(request):
    return render(request, "ervaringsdeskundige/register_investigation_succes.html")
