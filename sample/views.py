""" views.py """

from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import openai

def sample(request):
    return render(request, 'sample/chatgpt.html')


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






def setup(request):
    if request.method == 'POST':
        question = 'これから'+request.POST['topic']+'について、複数人と私でディベートします。 AさんBさんなどの私以外のひとはあなたが演じてください。 ではまず、Aさんの意見を述べて下さい。'
        response = openai.ChatCompletion.create(
            model='gpt-3.5-turbo',
            messages=[{'role':'user', 'content': question}],
        )
        logs.append({'user': 'ChatGPT', 'content': response['choices'][0]['message']['content']})
        return render(request,'ArguLink/discussion.html')
    return render(request,'ArguLink/discussion_setup.html')