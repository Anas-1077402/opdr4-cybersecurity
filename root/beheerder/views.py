from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from .forms import RegistratieFormulier
from django.http import JsonResponse
from django.contrib.admin.views.decorators import staff_member_required
from main.models import Organisaties, Onderzoeken, ErvaringsdeskundigeErvaringsdeskundige, Deelnames
from rest_framework.decorators import api_view
from django.template.loader import render_to_string
from beheerder.models import Beheerders
from ervaringsdeskundige.models import User


def home_view(request):
    return render(request, 'home.html')


@staff_member_required
def dashboard_beheerder(request):
    pending_admins = User.objects.filter(status=1).filter(is_staff=1)
    current_user = request.user
    return render(request, 'beheerder/dashboard/dashboard.html', {'pending_admins': pending_admins, 'user': current_user})


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
        print("check2")
        pending_admin.status = 2
        pending_admin.save()
        return redirect('/beheerder/dashboard')

    if action == 'declined':
        pending_admin.status = 3
        pending_admin.save()
        return redirect('/beheerder/dashboard')


@staff_member_required
def onderzoeken(request):
    onderzoeken = Onderzoeken.objects.values('titel', 'omschrijving','datum_vanaf', 'datum_tot', 'locatie', 'status', 'opmerkingen_beheerder', 'onderzoeks_id')

    return render(request, 'beheerder/onderzoeken.html', {'onderzoeken': onderzoeken})


@staff_member_required
def users(request):

    return render(request, 'beheerder/users.html')


def update_status(request, onderzoeks_id, nieuwe_status):
    print(f"Update status voor onderzoek {onderzoeks_id} naar {nieuwe_status}")
    onderzoek = Onderzoeken.objects.get(onderzoeks_id=onderzoeks_id)
    onderzoek.status = nieuwe_status
    onderzoek.save()
    return JsonResponse({'message': 'Status bijgewerkt'}, status=200)


def bewerk_onderzoek(request, onderzoeks_id):
    onderzoek = get_object_or_404(Onderzoeken, onderzoeks_id=onderzoeks_id)

    if request.method == 'POST':
        onderzoek.titel = request.POST['titel']
        onderzoek.omschrijving = request.POST['omschrijving']
        onderzoek.opmerkingen_beheerder = request.POST['opmerkingen_beheerder']
        onderzoek.status = request.POST['status']
        onderzoek.save()

        return redirect('/beheerder/onderzoeken')

    return render(request, 'beheerder/bewerk_onderzoek.html', {'onderzoek': onderzoek})


def verwijder_onderzoek(request, onderzoeks_id):
    onderzoek = get_object_or_404(Onderzoeken, onderzoeks_id=onderzoeks_id)

    if request.method == 'POST':
        onderzoek.delete()
        return redirect('onderzoeken')

    return render(request, 'beheerder/verwijder_onderzoek.html', {'onderzoek': onderzoek})


def user_list(request):
    beheerders = Beheerders.objects.all()
    ervaringsdeskundigen = User.objects.values('first_name', 'last_name', 'is_superuser', 'is_staff', 'date_joined')

    all_users = list(beheerders) + list(ervaringsdeskundigen)

    return render(request, 'beheerder/users.html', {'all_users': all_users})

@api_view(['GET'])
def get_dashboard(request):
    data = dict()
    list_research = Onderzoeken.objects.filter(status=1).select_related("organisatie")
    count_research = list_research.count()
    list_experience_expert = ErvaringsdeskundigeErvaringsdeskundige.objects.select_related("toezichthouder").filter(status=2)
    count_experience_expert = list_experience_expert.count()
    list_organization = Organisaties.objects.filter(status=1)
    count_organization = list_organization.count()
    list_attendance_request = Deelnames.objects.select_related('onderzoeks').select_related('ervaringsdeskundige').filter(status=1)
    print(list_attendance_request.get(pk=1).ervaringsdeskundige)
    count_attendance_request = list_attendance_request.count()

    context = {
        'research': list_research,
        'count_research': count_research,
        'experience_expert': list_experience_expert,
        'count_experience_expert': count_experience_expert,
        'organization': list_organization,
        'count_organization': count_organization,
        'attendance_request': list_attendance_request,
        'count_attendance_request': count_attendance_request,
    }

    data['research'] = render_to_string("beheerder/dashboard/dashboard_research.html", context, request)
    data['experience_expert'] = render_to_string("beheerder/dashboard/dashboard_experience_expert.html", context, request)
    data['organization'] = render_to_string("beheerder/dashboard/dashboard_organization.html", context, request)
    data['attendance_request'] = render_to_string("beheerder/dashboard/dashboard_attendance_request.html", context, request)
    return JsonResponse(data)