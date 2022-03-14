from django.shortcuts import render
from django.http import HttpResponseBadRequest, HttpResponseRedirect

from . import util
from .forms import *


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries(),
    })

def get_article(request, title):
    return render(request, "encyclopedia/article.html", {
        "article": util.get_entry(title),
        "title": title,
        "entries": util.list_entries(),
    })

def create_article(request):
    if request.method == "POST":
        form = CreateArticle(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            text = form.cleaned_data['text']
            entries = util.list_entries()
            if title not in entries:
                util.save_entry(title, text)
            else:
                return render(request, 'encyclopedia/articlealreadyexists.html')

        return HttpResponseRedirect(f'/wiki/{title}')
    else:
        form = CreateArticle()
        return render(request, 'encyclopedia/create.html', {
            'form': form,
            "entries": util.list_entries(),
        })

def edit_article(request, title):
    if request.method == "POST":
        form = EditArticle(request.POST)
        if form.is_valid():
            text = form.cleaned_data['text']
            util.save_entry(title, text)
            return HttpResponseRedirect(f'/wiki/{title}')
        return HttpResponseBadRequest()
    else:
        article = util.get_entry(title)
        form = EditArticle({'text': article})
        return render(request, 'encyclopedia/edit.html', {
            'form': form,
            "entries": util.list_entries(),
            'title': title
        })


def search(request):
    q = request.GET.get('q')
    entries = util.list_entries()
    results = []
    for entry in entries:
        lower_entry = entry.lower()
        lower_q = q.lower()
        if lower_entry.find(lower_q) != -1:
            results.append(entry)
    return render(request, 'encyclopedia/results.html', {
        'results': results,
        'entries': entries,
        'nothing': []
    })