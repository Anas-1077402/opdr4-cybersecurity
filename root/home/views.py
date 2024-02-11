from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from home.models import Organisatie, Onderzoeken
from home.serializers import OrganisatieSerializer, OnderzoekenSerializer


def index(request):
    return render(request, "home/index_test.html")


def login(request):
    return render(request, "home/login.html")


def register(request):
    return render(request, "home/register.html")


def API(request):
    if request.method == 'GET':
        all_organisaties = Organisatie.objects.all()
        serializer = OrganisatieSerializer(all_organisaties, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = OrganisatieSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


def organisatie_details(request, pk):
    try:
        organistatie = Organisatie.objects.get(pk=pk)
    except Organisatie.DoesNotExist:
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


def lijst_onderzoeken(request):
    if request.method == 'GET':
        onderzoeken_per_org = Onderzoeken.objects.filter(organistatie=2)
        serializer = OnderzoekenSerializer(onderzoeken_per_org, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = OnderzoekenSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
