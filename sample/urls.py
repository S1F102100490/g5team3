from django.urls import path
from . import views
from .views import generate_text
from .views import reading

app_name = 'sample'

urlpatterns = [
    path('', views.chatgpt, name='sample'),
    path('ask/', views.chatgpt, name='AskGPT'),
    path('generate_text/', views.chatgpt, name='generate_text'),
    path('reading/', views.reading, name='reading'),
]