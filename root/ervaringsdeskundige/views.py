from .forms import RegisterForm
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from ervaringsdeskundige.models import User
from .forms import RegisterForm
from main.models import Onderzoeken, Deelnames


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/') #word naar index gestuurd als succesvol ingevuld
    else:
        form = RegisterForm()
    return render(request, 'ervaringsdeskundige/register.html', {'form': form})


@login_required()
def dashboard_ervaringsdeskundige(request):
    current_user = request.user
    return render(request, 'ervaringsdeskundige/dashboard.html', {'user': current_user})

@login_required
def edit_profile(request):
    current_user = request.user
    if request.method == 'POST':
        form = RegisterForm(request.POST, instance=current_user)
        if form.is_valid():
            form.save()
            return redirect('/ervaringsdeskundige/dashboard')
    else:
        form = RegisterForm(instance=current_user)

    return render(request, 'ervaringsdeskundige/edit_profile.html', {'form': form})


def logout_ervaringsdeskundige(request):
    logout(request)
    return redirect("/login")

@login_required
def onderzoeken(request):
    investigations = Onderzoeken.objects.all()
    return render(request, 'ervaringsdeskundige/onderzoeken.html', {'investigations': investigations})

@login_required
def register_investigation(request, investigation_id):
    user_id = request.user.id

    new_register_investigation = Deelnames(ervaringsdeskundige_id=user_id, onderzoeks_id=investigation_id, status=2)
    new_register_investigation.save()

    return redirect('/ervaringsdeskundige/register_investigation_succes')

@login_required
def register_investigation_succes(request):
    return render(request, 'ervaringsdeskundige/register_investigation_succes.html')