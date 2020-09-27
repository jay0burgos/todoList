from django.db import models


#create adding, deleting and updating function

# class todoManager(models.Manager)

# class groupManager(models.Manager)
#     def default():
#         if :    #if a generic exists, which will be ID one return it
#             pass
#         else:
#             pass #else a hard coded genereic class will be created 

class toDo(models.Model):
    toDo = models.TextField()
    completed = models.BooleanField(default= False) #defaults to false when created
    date = models.DateField(blank=True) #doesnt need a date

# class groupings(models.Model):
#     name = models.CharField(max_length=40)
#     group = models.ForeignKey(toDo, on_delete=models.CASCADE)
