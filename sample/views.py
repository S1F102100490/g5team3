from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import openai
from .models import GeneratedText

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

        # ここでChatGPTとの対話を行い、文章を生成する処理を実装

        # 生成された文章をデータベースに保存
        generated_text = "Generated text"  # 仮の生成テキスト
        user_input = f"Length: {length}, Genre: {genre}"  # 仮のユーザー入力
        GeneratedText.objects.create(user_input=user_input, generated_text=generated_text)

        # 生成された文章をJSON形式で返す（適切な形式に変更）
        return JsonResponse({'generated_text': generated_text})

    return render(request, 'sample/chatgpt.html')
""" 
# sample/views.py

logs = []  # 会話のログを保持するリスト

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

        # 会話のログに追加
        logs.append({'user': 'You', 'content': question})
        logs.append({'user': 'ChatGPT', 'content': answer})

        # 応答をテンプレートに渡して表示
        return render(request, 'sample/chatgpt.html', {'logs': logs})
    
    return render(request, 'sample/chatgpt.html', {'logs': logs})

def generate_article(request):
    generated_article = ""  # 生成された文章を格納する変数を初期化

    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            # フォームデータを処理
            length = form.cleaned_data['length']
            genre = form.cleaned_data['genre']

            # ChatGPT との対話
            question = f"生成してほしい文章の長さは {length} で、ジャンルは {genre} です。"
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": question},
                ]
            )

            # 生成された文章を取得
            answer = response['choices'][0]['message']['content']
            generated_article = answer

    else:
        form = ArticleForm()

    return render(request, 'sample/chatgpt.html', {'form': form, 'article': generated_article})
 """