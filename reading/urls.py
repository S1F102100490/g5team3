from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.reading, name='Reading'),
    path('/make.html' , name='making'),
]