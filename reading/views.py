# reading/views.py
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import ArticleForm  # ArticleFormはフォームの定義
from .forms import ReadingForm

def reading(request):
    return render(request, 'reading/READING.html')


def article_result(request):
    return render(request, 'reading/article_result.html', {'article': 'Generated article will be displayed here.'})

# 仮想的な ChatGPT との連携関数
def generate_article_with_chatgpt(length, genre, happy_end):
    # ここで実際の ChatGPT との連携処理を行う
    # 例えば、OpenAI API を使用したり、ChatGPT サーバーにリクエストを送ったりする

    # 仮の実装: ダミーの文章を返す
    return f"Generated article with length: {length}, genre: {genre}, happy end: {happy_end}"


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