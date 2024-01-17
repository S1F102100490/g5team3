# views.py

from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
import openai
from .models import GeneratedText
from django.http import HttpResponse

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
    openai.api_key = "SPhexIGEF2VCHEkiBC1RnIhCmQb97438jbyBK0D-F84N7U_NCE8Iy0O40aPLg7RBSWKhIccjb_rbwqb82lSf1_Q"
    openai.api_base = "https://api.openai.iniad.org/api/v1"

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
    openai.api_key = "SPhexIGEF2VCHEkiBC1RnIhCmQb97438jbyBK0D-F84N7U_NCE8Iy0O40aPLg7RBSWKhIccjb_rbwqb82lSf1_Q"
    openai.api_base = "https://api.openai.iniad.org/api/v1"
    if request.method == 'POST':
        
        word_count = int(request.POST.get("length",""))
        genre = request.POST.get('genre', '')

        input_text = "Generate a kind of  {} article, the  words of article must be {} in easy English".format(genre, word_count)
        response = openai.ChatCompletion.create(

            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a English teacher, now you will generate aricle for your student"},
                {"role": "system", "content": " Your students are not good at studying English, please use easy English"},
                {"role": "user", "content": input_text},
            ]
        )

        generated_text = response['choices'][0]['message']['content']

        return render(request,"sample/reading.html",{"message": generated_text})

    return render(request,"sample/reading.html",{"message": generated_text})

