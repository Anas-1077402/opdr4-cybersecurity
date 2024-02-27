from .forms import RegisterForm
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from ervaringsdeskundige.models import Ervaringsdeskundige


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/') #word naar index gestuurd als succesvol ingevuld
    else:
        form = RegisterForm()
    return render(request, 'ervaringsdeskundige/register.html', {'form': form})


def login_ervaringsdeskundige(request):
    if request.user.is_authenticated:
        return redirect('/ervaringsdeskundige/dashboard')

    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        print(f"Username: {username}, Password: {password}")
        user = authenticate(request, username=username, password=password)
        print(user)
        if user is not None:
            login(request, user)
            return redirect('/ervaringsdeskundige/dashboard')
        else:
            print("het werkt niet")
            messages.success(request, ("Het inloggen ging fout"))
            return render(request, 'ervaringsdeskundige/login.html', {})

    else:
        return render(request, 'ervaringsdeskundige/login.html', {})


@login_required()
def dashboard_ervaringsdeskundige(request):
    current_user = request.user
    return render(request, 'ervaringsdeskundige/dashboard.html', {'user': current_user})
