from django.shortcuts import render
from django.http import HttpResponse


def reading(request):
    return render(request, 'reading/READING.html')
