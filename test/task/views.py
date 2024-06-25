from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# Articles de blog hardcodés
articles = [
    {'id': 1, 'title': 'Premier Article', 'content': 'Contenu du premier article'},
    {'id': 2, 'title': 'Deuxième Article', 'content': 'Contenu du deuxième article'},
    {'id': 3, 'title': 'Troisième Article', 'content': 'Contenu du troisième article'},
]

def article_list(request):
    return render(request, 'article_list.html', {'articles': articles})

def article_detail(request, article_id):
    article = next((article for article in articles if article['id'] == article_id), None)
    return render(request, 'article_detail.html', {'article': article})