from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from .forms import RegistratieFormulier
from django.contrib.auth.decorators import login_required

def home_view(request):
    return render(request, 'home.html')

@login_required()
def dashboard_beheerder(request):
    return render(request, 'beheerder/dashboard.html')

def signup(request):
    if request.method == 'POST':
        form = RegistratieFormulier(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('home/index_test.html')
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
            return redirect('beheerder/dashboard')

    else:
        return render(request, 'authentication/login.html', {})

def logout_beheerder(request):
    logout(request)
    return redirect("/login")
