from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from .forms import RegistratieFormulier
from django.contrib.admin.views.decorators import staff_member_required
from ervaringsdeskundige.models import User


def home_view(request):
    return render(request, 'home.html')

@staff_member_required
def dashboard_beheerder(request):
    pending_admins = User.objects.filter(status=1)
    current_user = request.user
    return render(request, 'beheerder/dashboard.html', {'pending_admins': pending_admins, 'user': current_user})


@staff_member_required
def edit_profile(request):
    current_user = request.user
    if request.method == 'POST':
        form = RegistratieFormulier(request.POST, instance=current_user)
        if form.is_valid():
            form.save()
            return redirect('/beheerder/dashboard')
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



def logout_beheerder(request):
    logout(request)
    return redirect("/login")


@staff_member_required
def change_status(request, user_id, action):
    pending_admin = get_object_or_404(User, id=user_id)
    if action == 'approved':
        pending_admin.status = 2
        pending_admin.save()
        redirect('dashboard')

    if action == 'declined':
        pending_admin.status = 3
        pending_admin.save()
        redirect('dashboard')
