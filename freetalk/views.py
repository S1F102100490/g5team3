from django.http.response import JsonResponse
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.http import Http404
from django.utils import timezone
from eng_app.models import Question
from eng_app.models import Answer
from django.contrib import messages
from django.db.models import Q
import requests
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def chat_with_gpt(request):
    if request.method == 'POST':
        user_input = request.POST.get('user_input')
        
        # ChatGPT APIへのリクエストを送信
        api_key = 'f3mwBbrkPeDVrxk28zfBLG-duFqTtdbDAzwaPenHBrQezi6RKMFgkim9SgYjYSCYzxsXWrzLk1XXlTgAqLQi0Lg'  # OpenAI APIキーを設定
        api_url = 'https://api.openai.com/v1/engines/davinci-codex/completions'
        headers = {
            'Authorization': f'Bearer {api_key}',
            'Content-Type': 'application/json',
        }
        data = {
            'prompt': user_input,
            'max_tokens': 50,  # 応答の最大トークン数を調整
        }
        
        response = requests.post(api_url, json=data, headers=headers)
        
        if response.status_code == 200:
            response_data = response.json()
            bot_response = response_data['choices'][0]['text']
            return JsonResponse({'bot_response': bot_response})
        else:
            return JsonResponse({'error': 'ChatGPT APIエラー'})
    return JsonResponse({'error': 'POSTリクエストが必要です'})

def freetalk(request):
    return render(request, 'freetalk/FreeTalk.html')