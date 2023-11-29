from django.urls import path
from . import views

urlpatterns = [
    path('', views.freetalk, name='FreeTalk'),
    path('ask/', views.chatgpt, name='AskGPT'),  # URLを'/ask/'から'/freetalk/ask/'に変更
]
