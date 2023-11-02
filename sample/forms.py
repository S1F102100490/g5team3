from django import forms

class ArticleForm(forms.Form):
    length = forms.IntegerField(label="文章の長さ")
    genre = forms.ChoiceField(choices=[("科学", "科学"), ("文学", "文学")], label="文章のジャンル")
