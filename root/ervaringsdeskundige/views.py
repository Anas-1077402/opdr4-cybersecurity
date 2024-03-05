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
from .models import BeperkingenOnderzoeken


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


@login_required()
def logout_ervaringsdeskundige(request):
    logout(request)
    return redirect("/login")


@login_required
def onderzoeken(request):
    user = request.user
    user_age = user.age()
    user_available_from = user.beschikbaar_vanaf
    user_available_until = user.beschikbaar_tot
    limitations_user = BeperkingenErvaringsdeskundigen.objects.filter(ervaringsdeskundigen_id=user.id)

    limitations_ids = limitations_user.values_list('beperking_id', flat=True)

    filtered_investigations = BeperkingenOnderzoeken.objects.filter(beperking_id__in=limitations_ids)
    filtered_investigations_ids = filtered_investigations.values_list('onderzoeks_id', flat=True)

    investigations = Onderzoeken.objects.filter(
        doelgroep_leeftijd_van__lte=user_age,
        doelgroep_leeftijd_tot__gte=user_age,
        datum_vanaf__lte=user_available_until,
        datum_tot__gte=user_available_from,
        onderzoeks_id__in=filtered_investigations_ids
    )

    investigations_with_limitations = {}

    for investigation in investigations:
        limitation_ids = BeperkingenOnderzoeken.objects.filter(onderzoeks_id=investigation.onderzoeks_id).values_list('beperking_id', flat=True)

        limitations = Beperkingen.objects.filter(id__in=limitation_ids)
        existing = Deelnames.objects.filter(ervaringsdeskundige_id=user, onderzoeks_id=investigation.onderzoeks_id)

        status = 0

        if existing:
            status = 1

        investigations_with_limitations[investigation.onderzoeks_id] = {
            'onderzoek': investigation,
            'beperkingen': limitations,
            'status': status,
        }

    return render(
        request,
        "ervaringsdeskundige/onderzoeken.html",
        {"investigations": investigations_with_limitations},
    )


@login_required
def registered_investigations(request):
    user_id = request.user.id

    current_investigations = Deelnames.objects.filter(ervaringsdeskundige_id=user_id)

    investigation_ids = current_investigations.values_list('onderzoeks_id', flat=True)

    investigations = Onderzoeken.objects.filter(onderzoeks_id__in=investigation_ids)

    investigations_with_limitations = {}

    for investigation in investigations:
        limitation_ids = BeperkingenOnderzoeken.objects.filter(onderzoeks_id=investigation.onderzoeks_id).values_list('beperking_id', flat=True)

        limitations = Beperkingen.objects.filter(id__in=limitation_ids)

        investigations_with_limitations[investigation.onderzoeks_id] = {
            'onderzoek': investigation,
            'beperkingen': limitations,
        }

    return render(
        request,
        "ervaringsdeskundige/registered_investigations.html",
        {"investigations": investigations_with_limitations},
    )


@login_required
def register_investigation(request, investigation_id):
    user_id = request.user.id

    existing = Deelnames.objects.filter(ervaringsdeskundige_id=user_id, onderzoeks_id=investigation_id)

    if not existing:
        new_register_investigation = Deelnames(
            ervaringsdeskundige_id=user_id, onderzoeks_id=investigation_id, status=2
        )
        new_register_investigation.save()

    return redirect("/ervaringsdeskundige/register_investigation_succes")


@login_required
def register_investigation_succes(request):
    return render(request, "ervaringsdeskundige/register_investigation_succes.html")


@login_required
def unsubscribe_investigation(request, investigation_id):
    user_id = request.user.id
    investigation_delete = Deelnames.objects.filter(ervaringsdeskundige_id=user_id, onderzoeks_id=investigation_id)
    investigation_delete.delete()
    return render(request, "ervaringsdeskundige/unsubscribe_investigation.html")


@login_required
def delete_account(request):
    comment = request.GET.get('comment')
    request.user.opmerking_verwijderd = comment
    request.user.status = 5
    request.user.save()
    logout(request)
    return redirect("/")
