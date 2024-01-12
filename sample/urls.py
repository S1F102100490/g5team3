from django.urls import path
from . import views
from .views import generate_text
from .views import reading

app_name = 'sample'  # 名前空間を指定

urlpatterns = [
    path('', views.chatgpt, name='sample'),
    path('ask/', views.chatgpt, name='AskGPT'),
    path('generate_text/', views.generate_text, name='generate_text'),
    path('reading/', views.reading, name='reading'),
]