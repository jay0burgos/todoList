from django.db.models import fields
from .models import toDo
from rest_framework import serializers


#very simililar to forms! you can even add create delete and update functions
class toDoSerializer(serializers.ModelSerializer): #quickstart has an issue her
    class Meta:
        model = toDo
        fields = ['toDoDiscrip' , 'completed']


    def create(self, validated_data):
        return toDo.objects.create(validated_data)
    
    def update(self, aToDo, validated_data):
        aToDo.toDoDiscrip = validated_data.get('toDoDiscrip', aToDo.toDoDiscrip)
        aToDo.completed = validated_data.get('completed', aToDo.completed)
        aToDo.date = validated_data.get('date', aToDo.date)
        aToDo.save()
        return aToDo