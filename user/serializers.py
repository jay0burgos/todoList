from django.db import models
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth.models import User
import bcrypt

class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required = True, validators= [UniqueValidator(queryset = User.objects.all())])
    username = serializers.CharField(max_length=32, validators=[UniqueValidator(queryset=User.objects.all())])
    password = serializers.CharField(min_length = 12, write_only=True)

    def create(self, validated_data):
        my_hash = bcrypt.hashpw(validated_data['password'].encode(), bcrypt.gensalt()).decode() #encription of the password 
        return User.objects.create_user(validated_data['username'], validated_data['email'], my_hash)
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')