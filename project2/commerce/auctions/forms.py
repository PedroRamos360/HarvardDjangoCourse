from django import forms
from .models import Category


class CreateListing(forms.Form):
    name = forms.CharField(label='Name', max_length=128)
    starting_bid = forms.FloatField(label='Starting Bid')
    description = forms.CharField(label='Product Description', widget=forms.Textarea, max_length=1024)
    image_url = forms.CharField(label='Image Url', required=False)
    categories = Category.objects.all()
    choices = []
    for category in categories:
        choices.append((category.id, category.name, ))
    choices = tuple(choices)
    category = forms.ChoiceField(choices=choices, required=False)


