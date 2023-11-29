from django.urls import path
from . import views

urlpatterns = [
    path('', views.chatgpt, name='sample'),
    path('ask/', views.chatgpt, name='AskGPT'),
]
