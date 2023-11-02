from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.generate_article, name='generate_article'),
]


""" path('', views.chatgpt, name='sample'), """