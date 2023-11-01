# reading/views.py
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import ArticleForm  # ArticleFormはフォームの定義
from .forms import ReadingForm

def reading(request):
    return render(request, 'reading/READING.html')



def generate_article(request):
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
