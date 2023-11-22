# reading/forms.py

from django import forms
from .models import Reading

class ReadingForm(forms.ModelForm):
    class Meta:
        model = Reading
        fields = ['title', 'content', 'genre', 'length']


class ArticleForm(forms.Form):
    length = forms.IntegerField(label="文章の長さ")
    genre = forms.ChoiceField(choices=[("科学", "科学"), ("文学", "文学")], label="文章のジャンル")
