from django.urls import path
from . import views

urlpatterns = [
    path('', views.sample, name='sample'),
    path('ask/', views.ask_question, name='ask_question'),
]