from django.shortcuts import render


def index(request):
    return render(request, "home/index_test.html")


def login(request):
    return render(request, "home/login.html")

def register(request):
    return render(request, "home/register.html")
