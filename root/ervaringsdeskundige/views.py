from .forms import RegisterForm
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from ervaringsdeskundige.models import User
from .forms import RegisterForm


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