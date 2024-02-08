from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from home.models import Organistatie
from home.serializers import OrganistatieSerializer

def index(request):
    return render(request, "home/index_test.html")


def login(request):
    return render(request, "home/login.html")

def register(request):
    return render(request, "home/register.html")

def API(request):
    if request.methods == 'GET':
        all_organisaties = Organistatie.objects.all()
        serializer = OrganistatieSerializer(all_organisaties, many=True)
        return JsonResponse(serializer.data, safe=False)
    
    elif request.methods == 'PUT':
        data = JSONParser().parse(request)
        serializer = OrganistatieSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

