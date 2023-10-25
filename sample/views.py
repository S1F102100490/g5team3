""" views.py """

from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import openai
import json

def sample(request):
    return render(request, 'sample\chatgpt.html')


@csrf_exempt
def ask_question(request):
    if request.method == 'POST':
        # POST リクエストのデータを JSON として読み込む
        data = json.loads(request.body.decode('utf-8'))
        question = data.get('question', '')

        openai.api_key = 'FXiCD7rJs-hPF-C9sPSYITe5gvxTiDpbBuiA3Yld-IZhcx1aLJNMLgPuNg0yodeIbedSpD5tXWHjJTERyT8BOTw'
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": question},
            ]
        )
        answer = response['choices'][0]['message']['content']
        return JsonResponse({'answer': answer})
 

""" 
def chat_view(request):
    if request.method == 'POST':
        user_message = request.POST.get('user_message', '')

        openai.api_key = 'FXiCD7rJs-hPF-C9sPSYITe5gvxTiDpbBuiA3Yld-IZhcx1aLJNMLgPuNg0yodeIbedSpD5tXWHjJTERyT8BOTw'
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": user_message},
            ]
        )
        chatgpt_response = response['choices'][0]['message']['content']

        return JsonResponse({'chatgpt_response': chatgpt_response})

    return render(request, 'templates/sample/chatgpt.html')
 """