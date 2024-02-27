from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from main.models import Organisaties, Onderzoeken
from main.serializers import OrganisatieSerializer, OnderzoekenSerializer


def index(request):
    return render(request, "home/index_test.html")


def login(request):
    return render(request, "home/login.html")


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
