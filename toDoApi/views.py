from django.db.models import query
from django.db.models.query import QuerySet
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import toDo
from .serializers import toDoSerializer
from django.shortcuts import render
from rest_framework import viewsets

#class base view
class toDoModelViewSet(viewsets.ModelViewSet):
    #simple viewSet that has actions already implemented
    #UPDATE!!!!!! add permission classes!!!!!!!!!
    queryset = toDo.objects.all()
    serializer_class = toDoSerializer

class toDoListViewSet(viewsets.ViewSet): #uses Viewset

    #LATER UPDATES- set permission by having a permission clas, look in dcumentation ViewSet

    #since im using viewset, I have to override actions and especify what they do!
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
            serializer.save() #uses serializer to create and save new entry
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




