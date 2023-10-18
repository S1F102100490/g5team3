from django.shortcuts import render
from django.http import HttpResponse


def speaking(request):
    return render(request, 'speaking/Speaking.html')
