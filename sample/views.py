# views.py

from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
import openai
from .models import GeneratedText

openai.api_key = settings.OPENAI_API_KEY

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




def reading(request):
    if request.method == 'POST':
        length = request.POST.get('length')
        genre = request.POST.get('genre')

        # ChatGPT との対話を行う処理
        chatgpt_response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=f"Generate text with length: {length}, genre: {genre}",
            max_tokens=int(length)
        )
        generated_text = chatgpt_response['choices'][0]['text']

        # 生成された文章をデータベースに保存
        user_input = f"Length: {length}, Genre: {genre}"
        GeneratedText.objects.create(user_input=user_input, generated_text=generated_text)

        # ChatGPT の応答も取得できるように追加
        answer = chatgpt_response['choices'][0]['message']['content']

        # Update the chat history in the session
        chat_history.append({"role": "user", "content": user_input})
        chat_history.append({"role": "assistant", "content": answer})
        request.session['chat_history'] = chat_history

        # 生成された文章をJSON形式で返す
        return JsonResponse({'generated_text': generated_text, 'assistant_response': answer})

    return render(request, 'sample/reading.html')




def generate_text(request):
    # Initialize or get the chat history from the session
    chat_history = request.session.get('chat_history', [])

    if request.method == 'POST':
        length = request.POST.get('length')
        genre = request.POST.get('genre')

        # ChatGPT との対話を行う処理
        chatgpt_response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=f"Generate text with length: {length}, genre: {genre}",
            max_tokens=int(length)
        )
        generated_text = chatgpt_response['choices'][0]['text']

        # 生成された文章をデータベースに保存
        user_input = f"Length: {length}, Genre: {genre}"
        GeneratedText.objects.create(user_input=user_input, generated_text=generated_text)

        # ChatGPT の応答も取得できるように追加
        answer = chatgpt_response['choices'][0]['message']['content']

        # Update the chat history in the session
        chat_history.append({"role": "user", "content": user_input})
        chat_history.append({"role": "assistant", "content": answer})
        request.session['chat_history'] = chat_history

        # 生成された文章をJSON形式で返す
        return JsonResponse({'generated_text': generated_text})

    return render(request, 'sample/chatgpt.html', {'chat_history': chat_history})