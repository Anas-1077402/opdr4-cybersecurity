from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import RegistratieFormulier

def home_view(request):
    return render(request, 'home.html')

def signup(request):
    if request.method == 'POST':
        form = RegistratieFormulier(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('home/index_test.html')
    else:
        form = RegistratieFormulier()
    return render(request, 'signup.html', {'form': form})