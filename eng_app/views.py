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

from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('your_home_view')  # ユーザーが登録したらホームページにリダイレクト
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('your_home_view')  # ログインしたらホームページにリダイレクト
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('your_logout_success_view')  # ログアウトしたら成功ページにリダイレクト