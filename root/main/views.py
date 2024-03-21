from django.template.loader import render_to_string
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from main.models import Organisaties, Onderzoeken
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login as auth_login, authenticate, logout
from django.contrib import messages
from main.serializers import OrganisatieSerializer, OnderzoekenSerializer
from rest_framework.response import Response



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

@api_view(['PUT'])
def update_onderzoek(request, onderzoeks_id):
    try:
        onderzoek = Onderzoeken.objects.get(pk=onderzoeks_id)
    except Onderzoeken.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'PUT':
        serializer = OnderzoekenSerializer(onderzoek, data=request.data, partial=True)
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
            onderzoeken_per_org = Onderzoeken.objects.filter(organisatie_id=organisation.organisatie_id)
            serializer = OnderzoekenSerializer(onderzoeken_per_org, many=True)
            return JsonResponse(serializer.data, safe=False)

        except Organisaties.DoesNotExist:
            return JsonResponse({'error': 'Ongeldige API-key'}, status=400)

    elif request.method == 'POST':
        try:
            organisation = Organisaties.objects.get(api_key=API_key)
            serializer = OnderzoekenSerializer(data=request.data, organisatie=organisation)
            if serializer.is_valid():
                serializer.save()
                print("test2")
                return JsonResponse(serializer.data, status=201)
            else:
                print("Validation errors:", serializer.errors)
                return JsonResponse(serializer.errors, status=400)

        except Organisaties.DoesNotExist:
            return JsonResponse({'error': 'Ongeldige API-key'}, status=400)

    return Response({'error': 'Onverwachte fout'}, status=500)
