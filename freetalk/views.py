from django.http.response import JsonResponse
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.http import Http404
from django.utils import timezone
from eng_app.models import Question
from eng_app.models import Answer
from django.contrib import messages
from django.db.models import Q


def freetalk(request):
    return render(request, 'freetalk/FreeTalk.html')