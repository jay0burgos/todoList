from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'toDo', views.toDoListViewSet, basename='toDo')

urlpatterns = [
    path('', include(router.urls)), #uses automatatic URL routing!
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
