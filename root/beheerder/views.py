from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render


def register(request):
    return render(request, "home/register.html")


def dashboard(request):
    return render(request, "home/index_test.html")


def login(request):
    return render(request, "home/login.html")
