from django import forms
from .models import Category


class CreateListing(forms.Form):
    categories = Category.objects.all()
    choices = []
    for category in categories:
        choices.append((category.id, category.name, ))
    choices = tuple(choices)
    name = forms.CharField(label='Name', max_length=128)
    starting_bid = forms.FloatField(label='Starting Bid')
    image_url = forms.CharField(label='Image Url', required=False)
    category = forms.ChoiceField(choices=choices, required=False)

