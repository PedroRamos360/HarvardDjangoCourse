from turtle import title
from django import forms


class CreateArticle(forms.Form):
    title = forms.CharField(label="Title", max_length=64)
    text = forms.CharField(label="Text", widget=forms.Textarea, max_length=8192)

class EditArticle(forms.Form):
    text = forms.CharField(label="Text", widget=forms.Textarea, max_length=8192)