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
    openai.api_key = "SPhexIGEF2VCHEkiBC1RnIhCmQb97438jbyBK0D-F84N7U_NCE8Iy0O40aPLg7RBSWKhIccjb_rbwqb82lSf1_Q"
    openai.api_base = "https://api.openai.iniad.org/api/v1"
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

            ]
        )

        answer = response['choices'][0]['message']['content']

        # 応答をテンプレートに渡して表示
        return render(request, 'sample/reading.html', {'question': user_question, 'answer': answer})

    return render(request, 'sample/reading.html')


def generate_text(request):
    openai.api_key = "SPhexIGEF2VCHEkiBC1RnIhCmQb97438jbyBK0D-F84N7U_NCE8Iy0O40aPLg7RBSWKhIccjb_rbwqb82lSf1_Q"
    openai.api_base = "https://api.openai.iniad.org/api/v1"

    if request.method == 'POST':
        word_count = int(request.POST.get('word_count', 100 ))
        genre = request.POST.get('genre', '')

        chat_prompt = "Generate an  article in English. Words: {}, Genre: {}".format(word_count,genre)

        response = openai.ChatCompletion.create(

            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You will be a teacher for beginner English student"},
                {"role": "system", "content": "Then please generate the Title"},
                {"role": "user", "content": chat_prompt},

            ]
        )

        generated_text = response['choices'][0]['message']['content']

        return render(request, "sample/reading.html", {"message": generated_text})

    return render(request,"sample/reading.html",{"message": generated_text})