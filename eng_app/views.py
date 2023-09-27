from django.http.response import JsonResponse
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.http import Http404
from django.utils import timezone
from eng_app.models import Question
from eng_app.models import Answer
from django.contrib import messages
from django.db.models import Q


def root(request):
    return HttpResponse('Hello Django')


def index(request):

	context={
		'questions':Question.objects.all(),
		'answers': Answer.objects.all()
	}
	return render(request, 'eng_app/index.html',context)


