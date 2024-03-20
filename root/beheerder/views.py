from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from .forms import RegistratieFormulier, UserEditForm, UserBeheerderForm
from django.http import JsonResponse, HttpResponse
from django.contrib.admin.views.decorators import staff_member_required
from main.models import Organisaties, Onderzoeken, User, Deelnames
from rest_framework.decorators import api_view
from django.template.loader import render_to_string
from main.serializers import OrganisatieSerializer, OnderzoekenSerializer, ExperienceExpertSerializer
from beheerder.models import Beheerders
from ervaringsdeskundige.models import User as TestUser
from django.db import transaction, connection
from django.db.models import Q



def home_view(request):
    return render(request, 'home.html')


@staff_member_required
def dashboard_beheerder(request):
    pending_admins = User.objects.filter(status=1).filter(is_staff=1)
    current_user = request.user
    return render(request, 'beheerder/dashboard/dashboard.html')


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

@staff_member_required
def update_status(request, onderzoeks_id, nieuwe_status):
    print(f"Update status voor onderzoek {onderzoeks_id} naar {nieuwe_status}")
    onderzoek = Onderzoeken.objects.get(onderzoeks_id=onderzoeks_id)
    onderzoek.status = nieuwe_status
    onderzoek.save()
    return JsonResponse({'message': 'Status bijgewerkt'}, status=200)

@staff_member_required
def update_organisatie_status(request, organisatie_id, nieuwe_status):
    print(f"Update status voor onderzoek {organisatie_id} naar {nieuwe_status}")
    organisatie = Organisaties.objects.get(organisatie_id=organisatie_id)
    organisatie.status = nieuwe_status
    organisatie.save()
    return JsonResponse({'message': 'Status bijgewerkt'}, status=200)

@staff_member_required
def update_ervaringsdeskundige_status(request, id, nieuwe_status):
    print(f"Update status voor onderzoek {id} naar {nieuwe_status}")
    ervaringsdeskundige = User.objects.get(id=id)
    ervaringsdeskundige.status = nieuwe_status
    ervaringsdeskundige.save()
    return JsonResponse({'message': 'Status bijgewerkt'}, status=200)

@staff_member_required
def update_deelnames_status(request, id, nieuwe_status):
    print(f"Update status voor onderzoek {id} naar {nieuwe_status}")
    deelnames = Deelnames.objects.get(id=id)
    deelnames.status = nieuwe_status
    deelnames.save()
    return JsonResponse({'message': 'Status bijgewerkt'}, status=200)


#def bewerk_onderzoek(request, onderzoeks_id):
#    onderzoek = get_object_or_404(Onderzoeken, onderzoeks_id=onderzoeks_id)

#    if request.method == 'POST':
#       onderzoek.titel = request.POST['titel']
#       onderzoek.omschrijving = request.POST['omschrijving']
#       onderzoek.opmerkingen_beheerder = request.POST['opmerkingen_beheerder']
#      onderzoek.status = request.POST['status']
#      onderzoek.save()

#       return redirect('/beheerder/onderzoeken')

#   return render(request, 'beheerder/bewerk_onderzoek.html', {'onderzoek': onderzoek})

@transaction.atomic
def verwijder_onderzoek(request, onderzoeks_id):
    onderzoek = Onderzoeken.objects.get(pk=onderzoeks_id)

    if request.method == 'POST':
        onderzoek.delete()
        return redirect('onderzoeken')

    return render(request, 'beheerder/verwijder_onderzoek.html', {'onderzoek': onderzoek})

@staff_member_required
def user_list(request):
    beheerders = Beheerders.objects.all()
    ervaringsdeskundigen = User.objects.values('id','first_name', 'last_name', 'is_superuser', 'is_staff', 'date_joined')

    all_users = list(beheerders) + list(ervaringsdeskundigen)

    return render(request, 'beheerder/users.html', {'all_users': all_users})

@staff_member_required
def search_users(request):
    query = request.GET.get('query', '')
    beheerders = Beheerders.objects.filter(Q(first_name__icontains=query) | Q(last_name__icontains=query)).all()
    ervaringsdeskundigen = TestUser.objects.filter(Q(first_name__icontains=query) | Q(last_name__icontains=query)).all()

    user_list = []
    for user in list(beheerders) + list(ervaringsdeskundigen):
        user_data = {
            'id': user.id,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'is_superuser': user.is_superuser,
            'is_staff': user.is_staff,
            'date_joined': user.date_joined.strftime("%Y-%m-%d %H:%M:%S"),
        }
        user_list.append(user_data)
    return JsonResponse({'users': user_list})

@staff_member_required
def user_delete(request, id):
    sql_query = "DELETE FROM ervaringsdeskundige_user WHERE id = %s"
    beheerder_sql_query = "DELETE FROM beheerder_beheerders WHERE id = %s"

    try:
      with transaction.atomic():
        with connection.cursor() as cursor:
            cursor.execute(sql_query, [id])
            cursor.execute(beheerder_sql_query, [id])

        return redirect('user_list')

    except Exception as e:
        return HttpResponse(f"Fout bij het verwijderen van gebruiker: {e}")

@staff_member_required
def user_edit(request, id):
    # hier gaat checked hij eerst of het beheerder is -> zo niet dan ervaringsdeskundige formulier
        if Beheerders.objects.filter(id=id).exists():
            user = get_object_or_404(Beheerders, id=id)
            if request.method == 'POST':
                form = UserBeheerderForm(request.POST, instance=user)
                if form.is_valid():
                    form.save()
                    return redirect('user_list')
        else:
            user = get_object_or_404(User, id=id)

        if request.method == 'POST':
            form = UserEditForm(request.POST, instance=user)
            if form.is_valid():
                form.save()
                return redirect('user_list')
        else:
            form = UserEditForm(instance=user)
        return render(request, 'beheerder/user_edit.html', {'form': form})


@staff_member_required
def dashboard(request):
    return render(request, "beheerder/dashboard/dashboard.html")


@staff_member_required
def research_item(request, pk):
    research_item_data = Onderzoeken.objects.filter(pk=pk).select_related("organisatie").get(pk=pk)
    context = {
        "data": research_item_data
    }
    return render(request, "beheerder/dashboard/dashboard_research_item.html", context)


@staff_member_required
def research_item_edit(request, pk):
    research_item_data = Onderzoeken.objects.filter(pk=pk).select_related("organisatie").get(pk=pk)

    # Converts datetime to value compatiable with html input=datetime-local element
    datetime_from = research_item_data.datum_vanaf
    datetime_till = research_item_data.datum_tot
    research_item_data.datum_vanaf = (str(datetime_from.date()) + 'T' + str(datetime_from.time()))
    research_item_data.datum_tot = (str(datetime_till.date()) + 'T' + str(datetime_till.time()))

    context = {
        "data": research_item_data
    }
    return render(request, "beheerder/dashboard/dashboard_research_item_edit.html", context)


@staff_member_required
def research_item_edit_save(request, pk):

    if request.method == 'POST':
        instance = Onderzoeken.objects.select_related("organisatie").get(pk=pk)
        data = request.POST
        serializer = OnderzoekenSerializer(instance, data)
        if serializer.is_valid():
            serializer.save()
            return redirect(f"/beheerder/dashboard/research/{pk}")
        return HttpResponse(status=400)
    return redirect(f"/beheerder/dashboard/research/{pk}")


@staff_member_required
def experience_expert_item(request, pk):
    experience_expert_item_data = User.objects.get(pk=pk)
    context = {
        "data": experience_expert_item_data
    }
    return render(request, "beheerder/dashboard/dashboard_experience_expert_item.html", context)


@staff_member_required
def experience_expert_item_edit(request, pk):
    experience_expert_item_data = User.objects.get(pk=pk)
    experience_expert_item_data.geboortedatum = str(experience_expert_item_data.geboortedatum)
    context = {
        "data": experience_expert_item_data
    }
    return render(request, "beheerder/dashboard/dashboard_experience_expert_item_edit.html", context)


@staff_member_required
def experience_expert_item_edit_save(request, pk):
    if request.method == 'POST':
        instance = User.objects.get(pk=pk)
        data = request.POST
        serializer = ExperienceExpertSerializer(instance, data)
        if serializer.is_valid():
            serializer.save()
            return redirect(f"/beheerder/dashboard/experience_expert/{pk}")
        return HttpResponse(status=400)
    return redirect(f"/beheerder/dashboard/experience_expert/{pk}")


@staff_member_required
def organization_item(request, pk):
    organization_item_data = Organisaties.objects.get(pk=pk)
    context = {
        "data": organization_item_data
    }
    return render(request, "beheerder/dashboard/dashboard_organization_item.html", context)


@staff_member_required
def organization_item_edit(request, pk):
    organization_item_data = Organisaties.objects.get(pk=pk)
    context = {
        "data": organization_item_data
    }
    return render(request, "beheerder/dashboard/dashboard_organization_item_edit.html", context)


@staff_member_required
def organization_item_edit_save(request, pk):
    if request.method == 'POST':
        instance = Organisaties.objects.get(pk=pk)
        data = request.POST
        serializer = OrganisatieSerializer(instance, data)
        if serializer.is_valid():
            serializer.save()
            return redirect(f"/beheerder/dashboard/organization/{pk}")
        print(serializer.errors)
        return HttpResponse(status=400)
    return redirect(f"/beheerder/dashboard/organization/{pk}")


@staff_member_required
def attendance_request_item(request, pk):
    attendance_request_item_data = Deelnames.objects.select_related('onderzoeks').select_related('ervaringsdeskundige').get(pk=pk)

    context = {
        "data": attendance_request_item_data,
    }

    return render(request, "beheerder/dashboard/dashboard_attendance_request_item.html", context)


@staff_member_required
def attendance_request_item_edit(request, pk):
    attendance_request_item_data = Deelnames.objects.select_related('onderzoeks').select_related('ervaringsdeskundige').get(pk=pk)
    context = {
        "data": attendance_request_item_data
    }
    return render(request, "beheerder/dashboard/dashboard_attendance_request_item_edit.html", context)


@staff_member_required
def attendance_request_item_edit_save(request, pk):
    if request.method == 'POST':
        instance = Deelnames.objects.select_related('onderzoeks').select_related('ervaringsdeskundige').get(pk=pk)
        data = request.POST
        if data['status']:
            instance.status = data['status']
            instance.save()
            return redirect(f"/beheerder/dashboard/attendance_request/{pk}")
        return HttpResponse(status=400)
    return redirect(f"/beheerder/dashboard/attendance_request/{pk}")

@staff_member_required
@api_view(['GET'])
def get_dashboard(request):
    data = dict()
    list_research = Onderzoeken.objects.filter(status=1).select_related("organisatie")
    count_research = list_research.count()
    list_experience_expert = User.objects.filter(status=1)
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

