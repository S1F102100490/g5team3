""" from django.http.response import JsonResponse
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.http import Http404
from django.utils import timezone
from eng_app.models import Question
from eng_app.models import Answer
from django.contrib import messages
from django.db.models import Q """


from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import openai


def freetalk(request):
    return render(request, 'freetalk/FreeTalk.html')




def chatgpt(request):
    if request.method == 'POST':
        question = request.POST.get('question', '')

        # ChatGPTとの対話
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": question},
            ]
        )

        answer = response['choices'][0]['message']['content']

        # 応答をテンプレートに渡して表示
        return render(request, 'freetalk/FreeTalk.html', {'question': question, 'answer': answer})

    return render(request, 'freetalk/FreeTalk.html')

