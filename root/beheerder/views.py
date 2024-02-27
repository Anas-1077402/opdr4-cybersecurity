from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from .forms import RegistratieFormulier
from django.contrib.auth.decorators import login_required
from beheerder.models import Beheerders


def home_view(request):
    return render(request, 'home.html')

@login_required()
def dashboard_beheerder(request):
    pending_admins = Beheerders.objects.filter(status=1)
    current_user = request.user
    return render(request, 'beheerder/dashboard.html', {'pending_admins': pending_admins, 'user': current_user})


@login_required()
def edit_profile(request):
    current_user = request.user
    if request.method == 'POST':
        form = RegistratieFormulier(request.POST, instance=current_user)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = RegistratieFormulier(instance=current_user)

    return render(request, 'beheerder/edit_profile.html', {'form': form})


def signup(request):
    if request.method == 'POST':
        form = RegistratieFormulier(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/home/index_test.html')
    else:
        form = RegistratieFormulier()
    return render(request, 'beheerder/signup.html', {'form': form})


def login_beheerder(request):
    if request.user.is_authenticated:
        return redirect('dashboard')

    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        if user is not None and user.status == 2:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.success(request, ("Het inloggen ging fout"))
            return render(request, 'beheerder/login.html', {})

    else:
        return render(request, 'beheerder/login.html', {})


def logout_beheerder(request):
    logout(request)
    return redirect("/beheerder/login-beheerder")


def change_status(request, user_id, action):
    pending_admin = get_object_or_404(Beheerders, id=user_id)
    if action == 'approved':
        pending_admin.status = 2
        pending_admin.save()
        redirect('dashboard')

    if action == 'declined':
        pending_admin.status = 3
        pending_admin.save()
        redirect('dashboard')
