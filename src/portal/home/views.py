from django.shortcuts import render
import urllib.request
from django.http import HttpResponse
from django.template import loader
from .news import wiki_news


# Create your views here.

def home(request):
    context = {}
    template = loader.get_template('home.html')
    result = wiki_news()
    context['wiki_news'] = result
    return HttpResponse(template.render(context, request))



