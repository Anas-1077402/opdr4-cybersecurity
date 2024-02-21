from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from .forms import RegistratieFormulier
from django.contrib.auth.decorators import login_required
from beheerder.models import CustomUser

def home_view(request):
    return render(request, 'home.html')

@login_required()
def dashboard_beheerder(request):
    pending_admins = CustomUser.objects.filter(status=1)
    return render(request, 'beheerder/dashboard.html', {'pending_admins': pending_admins})

def signup(request):
    if request.method == 'POST':
        form = RegistratieFormulier(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('/home/index_test.html')
    else:
        form = RegistratieFormulier()
    return render(request, 'signup.html', {'form': form})


def login_beheerder(request):
    print("test")
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            print("dit gaat goed")
            return redirect('dashboard')
        else:
            print("dit gaat fout")
            messages.success(request, ("Het inloggen ging fout"))
            return render(request, 'authentication/login.html', {})
    else:
        return render(request, 'authentication/login.html', {})

def logout_beheerder(request):
    logout(request)
    return redirect("/login")


def change_status(request, user_id, action):
    pending_admin = get_object_or_404(CustomUser, id=user_id)
    print("test")
    if action == 'approved':
        pending_admin.status = 2
        pending_admin.save()
        redirect('dashboard')

    if action == 'declined':
        pending_admin.status = 3
        pending_admin.save()
        redirect('dashboard')
