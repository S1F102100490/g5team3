from django.shortcuts import render
from django.http import HttpResponse

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import openai

def sample(request):
    return render(request, 'sample/chatgpt.html')


@csrf_exempt
def ask_question(request):
    if request.method == 'POST':
        question = request.POST.get('question', '')
        openai.api_key = 'Zi1YPAX8zfVUxvvYRCGFx6o1A-Nmz4Ad_-_DpF-NKPddxPKJCftXOF10tjYhpe4mxaSf4Se99LUKJG1xn73lwGA'
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": question},
            ]
        )
        answer = response['choices'][0]['message']['content']
        return JsonResponse({'answer': answer})
