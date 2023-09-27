from django.urls import path
from . import views

urlpatterns = [
    path('', views.freetalk, name='FreeTalk'),
]