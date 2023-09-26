from django.urls import path
from . import views

urlpatterns = [
	path('Home', views.home, name='Home'),
    path('', views.reading, name='Reading'),
    path('FreeTalk', views.freetalk, name='FreeTalk'),
]