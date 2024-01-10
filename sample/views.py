from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import openai
from .models import GeneratedText

openai.api_key = 'JEASLG20yKVDNCKvsosyuMcH-u5MRvkH2CUJ1LgxcyYR2VIkoRAJaJ3iGGfWLWStWIScV3-4q4p3vSGFXI0IwTw '

def sample(request):
    return render(request, 'sample\chatgpt.html')

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


def generate_text(request):
    if request.method == 'POST':
        length = request.POST.get('length')
        genre = request.POST.get('genre')

        # ChatGPT との対話を行う処理
        # 以下は仮の例。実際には ChatGPT API を呼び出して結果を取得する必要があります。
        # また、ChatGPT API を使用する際には適切な API キーを設定してください。
        chatgpt_response = openai.Completion.create(
            engine="text-davinci-003",  # 使用する ChatGPT エンジン
            prompt=f"Generate text with length: {length}, genre: {genre}",
            max_tokens=int(length)  # 生成する文章の長さを指定
        )
        generated_text = chatgpt_response['choices'][0]['text']

        # 生成された文章をデータベースに保存
        user_input = f"Length: {length}, Genre: {genre}"
        GeneratedText.objects.create(user_input=user_input, generated_text=generated_text)

        # 生成された文章をJSON形式で返す（適切な形式に変更）
        return JsonResponse({'generated_text': generated_text})

    return render(request, 'sample/chatgpt.html')

def reading(request):
    if request.method == 'POST':
        length = request.POST.get('length')
        genre = request.POST.get('genre')

        # ここでChatGPTとの対話を行い、文章を生成する処理を実装

        # 生成された文章をデータベースに保存
        generated_text = "Generated text"  # 仮の生成テキスト
        user_input = f"Length: {length}, Genre: {genre}"  # 仮のユーザー入力
        GeneratedText.objects.create(user_input=user_input, generated_text=generated_text)

        # 生成された文章をJSON形式で返す（適切な形式に変更）
        return JsonResponse({'generated_text': generated_text})

    return render(request, 'sample/reading.html')
