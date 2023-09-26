from django.urls import path
from . import views

urlpatterns = [
	path('', views.home, name='Home'),
    path('', views.reading, name='Reading'),
    path('', views.freetalk, name='Freetalk'),
]