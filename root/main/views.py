from django.template.loader import render_to_string
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from main.models import Organisaties, Onderzoeken, ErvaringsdeskundigeErvaringsdeskundige, Deelnames
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login as auth_login, authenticate, logout
from django.contrib import messages
from main.serializers import OrganisatieSerializer, OnderzoekenSerializer

def index(request):
    return render(request, "home/index_test.html")

def custom_login(request):
    if request.user.is_authenticated and request.user.is_staff == 1:
        return redirect('/beheerder/dashboard')

    if request.user.is_authenticated and request.user.is_staff == 0:
        return redirect('/ervaringsdeskundige/dashboard')

    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        print(user)
        if user is not None and user.status == 2:
            auth_login(request, user)
            if request.user.is_authenticated and request.user.is_staff == 1:
                return redirect('/beheerder/dashboard')

            if request.user.is_authenticated and request.user.is_staff == 0:
                return redirect('/ervaringsdeskundige/dashboard')
        else:
            messages.success(request, ("Het inloggen ging fout"))
            return render(request, 'home/login.html', {})

    else:
        return render(request, 'home/login.html', {})


def register(request):
    return render(request, "home/register.html")


def dashboard(request):
    return render(request, "beheerder/dashboard/dashboard.html")


def research_item(request, pk):
    research_item_data = Onderzoeken.objects.filter(pk=pk).select_related("organisatie").get(pk=pk)
    context = {
        "data": research_item_data
    }
    return render(request, "beheerder/dashboard/dashboard_research_item.html", context)


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


def research_item_edit_save(request, pk):

    if request.method == 'POST':
        instance = Onderzoeken.objects.select_related("organisatie").get(pk=pk)
        data = request.POST
        test = OnderzoekenSerializer(instance, data)
        if test.is_valid():
            test.save()
            return redirect(f"/beheerder/dashboard/research/{pk}")
        return HttpResponse(test.errors, 400)
    return redirect(f"/beheerder/dashboard/research/{pk}")


def experience_expert_item(request, pk):
    experience_expert_item_data = ErvaringsdeskundigeErvaringsdeskundige.objects.filter(pk=pk).select_related("toezichthouder").get(pk=pk)
    context = {
        "data": experience_expert_item_data
    }
    return render(request, "beheerder/dashboard/dashboard_experience_expert_item.html", context)


def experience_expert_item_edit(request, pk):
    experience_expert_item_data = ErvaringsdeskundigeErvaringsdeskundige.objects.filter(pk=pk).select_related("toezichthouder").get(pk=pk)
    context = {
        "data": experience_expert_item_data
    }
    return render(request, "beheerder/dashboard/dashboard_experience_expert_item_edit.html", context)


def experience_expert_item_edit_save(request, pk):
    """
    if request.method == 'POST':
        research_item_data = Onderzoeken.objects.filter(pk=pk).select_related("organisatie")
    context = {
        "data": research_item_data
    }
    """
    return redirect(f"/beheerder/dashboard/experience_expert/{pk}")


def organization_item(request, pk):
    organization_item_data = Organisaties.objects.get(pk=pk)
    context = {
        "data": organization_item_data
    }
    return render(request, "beheerder/dashboard/dashboard_organization_item.html", context)


def organization_item_edit(request, pk):
    organization_item_data = Organisaties.objects.get(pk=pk)
    context = {
        "data": organization_item_data
    }
    return render(request, "beheerder/dashboard/dashboard_organization_item_edit.html", context)


def organization_item_edit_save(request, pk):
    """
    if request.method == 'POST':
        research_item_data = Onderzoeken.objects.filter(pk=pk).select_related("organisatie")
    context = {
        "data": research_item_data
    }
    """
    return redirect(f"/beheerder/dashboard/organization/{pk}")


def attendance_request_item(request, pk):
    attendance_request_item_data = Deelnames.objects.select_related('onderzoeks').select_related('ervaringsdeskundige').get(pk=pk)
    context = {
        "data": attendance_request_item_data
    }
    return render(request, "beheerder/dashboard/dashboard_attendance_request_item.html", context)


def attendance_request_item_edit(request, pk):
    attendance_request_item_data = Deelnames.objects.select_related('onderzoeks').select_related('ervaringsdeskundige').get(pk=pk)
    context = {
        "data": attendance_request_item_data
    }
    return render(request, "beheerder/dashboard/dashboard_attendance_request_item_edit.html", context)


def attendance_request_item_edit_save(request, pk):
    """
    if request.method == 'POST':
        research_item_data = Onderzoeken.objects.filter(pk=pk).select_related("organisatie")
    context = {
        "data": research_item_data
    }
    """
    return redirect(f"/beheerder/dashboard/attendance_request/{pk}")


@api_view(['GET'])
def get_dashboard(request):
    data = dict()
    list_research = Onderzoeken.objects.filter(status=1).select_related("organisatie")
    count_research = list_research.count()
    list_experience_expert = ErvaringsdeskundigeErvaringsdeskundige.objects.filter(status=2).select_related("toezichthouder")
    count_experience_expert = list_experience_expert.count()
    list_organization = Organisaties.objects.filter(status=1)
    count_organization = list_organization.count()
    list_attendance_request = Deelnames.objects.filter(status=1).select_related('onderzoeks').select_related('ervaringsdeskundige')
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


@api_view(['GET', 'POST'])
def API(request):
    if request.method == 'GET':
        all_organisaties = Organisaties.objects.all()
        serializer = OrganisatieSerializer(all_organisaties, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = OrganisatieSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@api_view(['GET', 'POST', 'PUT'])
def organisatie_details(request, pk):
    try:
        organistatie = Organisaties.objects.get(pk=pk)
    except Organisaties.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = OrganisatieSerializer(organistatie)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        serializer = OrganisatieSerializer(organistatie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)


@api_view(['GET', 'POST'])
def lijst_onderzoeken(request):
    API_key = request.GET.get('api')

    if request.method == 'GET':
        try:
            organisation = Organisaties.objects.get(api_key=API_key)

            organisation_id = organisation.organisatie_id

            onderzoeken_per_org = Onderzoeken.objects.filter(organisatie_id=organisation_id)
            serializer = OnderzoekenSerializer(onderzoeken_per_org, many=True)
            return JsonResponse(serializer.data, safe=False)

        except Organisaties.DoesNotExist:
            return JsonResponse({'error': 'Ongeldige API-key'}, status=400)

    elif request.method == 'POST':
        try:
            Organisaties.objects.get(api_key=API_key)

            data = JSONParser().parse(request)
            serializer = OnderzoekenSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data, status=201)

        except Organisaties.DoesNotExist:
            return JsonResponse({'error': 'Ongeldige API-key'}, status=400)
