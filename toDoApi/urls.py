from django.urls import path
from . import views
urlpatterns = [
    path('toDo/', views.toDo_list),
    path('toDo/<int:toDoID>', views.toDo_details),
]
