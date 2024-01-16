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

# views.py

def reading(request):
    if request.method == 'POST':
        length = request.POST.get('length', '')
        genre = request.POST.get('genre', '')
        user_question = request.POST.get('question', '')

        # ChatGPTとの対話
        chat_prompt = f"Generate an English text. Length: {length}, Genre: {genre}"
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": user_question},
                {"role": "assistant", "content": chat_prompt},
            ]
        )

        answer = response['choices'][0]['message']['content']

        # 応答をテンプレートに渡して表示
        return render(request, 'sample/reading.html', {'question': user_question, 'answer': answer})

    return render(request, 'sample/reading.html')


def generate_text(request):
    if request.method == 'POST':
        word_count = int(request.POST.get('word_count', 50))
        genre = request.POST.get('genre', '科学')

        openai.api_key = 'YOUR_OPENAI_API_KEY'

        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=f"Write a {genre} text with {word_count} words:",
            max_tokens=word_count
        )

        generated_text = response.choices[0].text.strip()

        return HttpResponse(generated_text)

    return HttpResponse('Invalid Request')