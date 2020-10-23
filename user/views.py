from django.shortcuts import render
from rest_framework.serializers import Serializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from user.serializers import UserSerializer
from django.contrib.auth.models import User



class UserCreate(APIView):


    def post(self, request, format='json'):
        Serializer = UserSerializer(data=request.data) #serializer object
        if Serializer.is_valid():
            user = Serializer.save()
            if user:
                return Response(Serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(Serializer.errors, status=status.HTTP_400_BAD_REQUEST) #handles the bad request