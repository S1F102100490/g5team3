# views.py

from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
import openai
from .models import GeneratedText
from django.http import HttpResponse

openai.api_key = settings.OPENAI_API_KEY
openai.api_key = 'JEASLG20yKVDNCKvsosyuMcH-u5MRvkH2CUJ1LgxcyYR2VIkoRAJaJ3iGGfWLWStWIScV3-4q4p3vSGFXI0IwTw '

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
        return render(request, 'sample/chatgpt.html', {'question': question, 'answer': answer})

    return render(request, 'sample/chatgpt.html')



# views.py

def reading(request):
    if request.method == 'POST':
        length = request.POST.get('length', '')
        genre = request.POST.get('genre', '')
        user_question = request.POST.get('question', '')

        # ChatGPTとの対話
        chat_prompt = f"文章の長さは{length}, ジャンルは{genre}でお願いします。"
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "あなたは物語を作る著者です。会話への応答は文章のタイトルと文章の内容のみで結構です。"},
                {"role": "user", "content": user_question},
                {"role": "assistant", "content": chat_prompt},
            ]
        )

        answer = response['choices'][0]['message']['content']

        # 応答をテンプレートに渡して表示
        return render(request, 'sample/reading.html', {'answer': answer})

    return render(request, 'sample/reading.html')


def generate_text(request):
    if request.method == 'POST':
        word_count = int(request.POST.get('word_count', 50))
        genre = request.POST.get('genre', '')


        response = openai.ChatCompletion.create(

            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": f"Write a {genre} text with {word_count} words:"},
            ]
        )

        generated_text = response['choices'][0]['message']['content']

        return render(request,"sample/reading.html",{"generated_text": generated_text})

    return render(request,"sample/reading.html",{"generated_text": generated_text})

