"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
import eng_app.views
from reading import views as reading_views


urlpatterns = [
    path('Reading/', include('reading.urls')),
    path('FreeTalk/', include('freetalk.urls')),
    path('Speaking/', include('speaking.urls')),
    path( "", include("eng_app.urls")),
    path('sample/', include('sample.urls')),
    path('ask_sample/', include('sample.urls')),
    path('ask_freeatlk/', include('freetalk.urls')),
    path('ask_reading/', include('reading.urls')),
    path( "signup", include("eng_app.urls")),
    path( "login", include("eng_app.urls")),
    path( "logout", include("eng_app.urls")),
]
