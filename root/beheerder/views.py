from .forms import BeheerderForm
from django.shortcuts import render, redirect

def register(request):
    if request.method == 'POST':
        form = BeheerderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home/index_test.html')
    else:
        form = BeheerderForm()

    return render(request, 'signup.html', {'form': form})



def dashboard(request):
    return render(request, "home/index_test.html")


def login(request):
    return render(request, "home/login.html")
