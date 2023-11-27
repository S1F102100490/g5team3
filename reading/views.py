# reading/views.py
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import ArticleForm  # ArticleFormはフォームの定義
from .forms import ReadingForm
import openai

openai.api_key = 'JEASLG20yKVDNCKvsosyuMcH-u5MRvkH2CUJ1LgxcyYR2VIkoRAJaJ3iGGfWLWStWIScV3-4q4p3vSGFXI0IwTw'

def reading(request):
    return render(request, 'reading/READING.html')


def article_result(request):
    return render(request, 'reading/article_result.html', {'article': 'Generated article will be displayed here.'})

def generate_article_with_chatgpt(length, genre, happy_end):
    try:
        # ChatGPT へのリクエストパラメータの構築
        prompt = f"Generate an article with {length} words, in the {genre} genre, with a {'happy' if happy_end == 'yes' else 'not happy'} ending."

        # OpenAI API を使用して ChatGPT に文章生成のリクエストを送る
        response = openai.Completion.create(
            engine="text-davinci-003",  # GPT-3.5-turbo エンジンを指定
            prompt=prompt,
            max_tokens=400,  # 生成される文章の最大トークン数を指定
            temperature=0.7  # 生成のランダム性を調整するための temperature パラメータ
        )

        # API レスポンスから生成された文章を取得
        generated_article = response.choices[0].text.strip()
        return generated_article

    except Exception as e:
        # エラーが発生した場合の処理
        return f"Error generating article: {str(e)}"

def generate_article(request):
    if request.method == 'POST':
        length = request.POST.get('length')
        genre = request.POST.get('genre')
        happy_end = request.POST.get('happy_end')

        # ここでChatGPTにリクエストを送り、生成された文章を取得する処理を実装
        generated_article = generate_article_with_chatgpt(length, genre, happy_end)

        return render(request, 'reading/article_result.html', {'article': generated_article})

    return HttpResponse("Invalid Request")




""" def generate_article(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            # フォームデータを処理
            length = form.cleaned_data['length']
            genre = form.cleaned_data['genre']
            # データをChatGPTに送信し文章生成
            # ...
            # 生成された文章をテンプレートに渡す
            return render(request, 'reading/result.html', {'article': generated_article})
    else:
        form = ArticleForm()
    return render(request, 'reading/generate_article.html', {'form': form})
 """