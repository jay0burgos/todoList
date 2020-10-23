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
    toDoDiscrip = models.TextField()
    completed = models.BooleanField(default= False) #defaults to false when created
    date = models.DateField(null=True, blank=True) 
    


    # class Meta: used to remove parent attributes in child 
        
# class groupings(models.Model):
#     name = models.CharField(max_length=40)
#     group = models.ForeignKey(toDo, on_delete=models.CASCADE)
