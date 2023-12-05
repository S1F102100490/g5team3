from django import forms

class ChatForm(forms.Form):

    sentence = forms.CharField(label="Chat",widget=forms.Textarea(), required=True)