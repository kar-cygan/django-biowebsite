from django.shortcuts import render
from decouple import config
import requests

SOURCES = [
    {'id': 'new-scientist', 'name': 'New Scientist'},
    {'id': 'national-geographic', 'name': 'National Geographic'},
    {'id': 'medical-news-today', 'name': 'Medical News Today'},
    {'id': 'next-big-future', 'name': 'Next Big Future'},
]

def news_view(request, source='new-scientist'):
    api_key = config('API_KEY')
    url = f'https://newsapi.org/v2/everything?sources={source}&apiKey={api_key}'
    response = requests.get(url)
    data = response.json()
    context = {
        'sources': SOURCES,
        'active_source': source,
        'newsapi': data
    }
    return render(request, 'news/index.html', context)
