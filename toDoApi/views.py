from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import toDo
from .serializers import toDoSerializer
from django.shortcuts import render
from rest_framework import viewsets

#class base view

class toDoListViewSet(viewsets.ViewSet): #uses View set to 

    @csrf_exempt #allows to get a request using the viewset routing
    def list(self,request):
        toDoList = toDo.objects.all()
        serializer = toDoSerializer(toDoList, many = True)
        return JsonResponse(serializer.data, safe=False)
    def create(self, request):
        data = JSONParser().parse(request)
        serializer = toDoSerializer(data = data)
            #must check if data within serializer is valid
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status = 201) #once validated it will return it
        else:
            return JsonResponse(serializer.errors, status = 400)    

    def retrieve(self, request, pk):
        try:
            toDoItem = toDo.objects.get(id = pk)
        except toDoItem.DoesNotExist:
            return HttpResponse(status =404)
        
        if request.method == 'GET':
            serializer = toDoSerializer(toDoItem)
            return JsonResponse(serializer.data) #returns the specified data




