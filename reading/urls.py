from django.urls import path
from . import views

urlpatterns = [
    path('', views.reading, name='Reading'),
    path('ask/', views.chatgpt, name='AskGPT'),
]