from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'reading/Home.html')

def reading(request):
    return render(request, 'reading/Reading.html')

def freetalk(request):
    return render(request, 'reading/FreeTalk.html')
