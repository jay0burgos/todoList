from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import toDo
from .serializers import toDoSerializer
from django.shortcuts import render

@csrf_exempt
def toDo_list(request):
    if request.method == 'GET':
        toDoList = toDo.objects.all()
        serializer = toDoSerializer(toDoList, many = True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = toDoSerializer(data = data)
        #must check if data within serializer is valid
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status = 201)
        else:
            return JsonResponse(serializer.errors, status = 400)
            

