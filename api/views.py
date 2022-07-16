from django.shortcuts import render , HttpResponse
from .models import Person
from .serializers import PersonSerializer
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
# Create your views here.


def Index(request):
    return HttpResponse("Hello there!")


def person_list(request):
    # get all persons
    if request.method == 'GET':
        persons = Person.objects.all()
        serializer = PersonSerializer(persons , many= True)

        return JsonResponse(serializer.data , safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = PersonSerializer(data= data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data , status=201)
    return JsonResponse(serializer.errors , status= 400)
