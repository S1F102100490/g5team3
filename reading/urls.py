from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name='HOME'),
    path('', views.index, name='READING'),
    path('', views.index, name='FREE TALK'),
]