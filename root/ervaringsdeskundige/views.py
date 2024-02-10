from django.shortcuts import render, redirect
from .forms import RegisterForm


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login.html') #word naar login gestuurd als succesvol ingevuld
    else:
        form = RegisterForm()
    return render(request, 'home/register.html', {'form': form})
