from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.reading, name='Reading'),
    path('generate_article/', views.generate_article, name='generate_article'),
    path('article_result/', views.article_result, name='article_result'),
    path('ask/', views.chatgpt, name='AskGPT'),
]
