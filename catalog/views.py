from django.shortcuts import render
import requests
from django.conf import settings
from .models import Articles, Author, Genre
# прописываем логику в обьект request 
def index(request):
    num_articles=Articles.objects.all().count()
    num_authors=Author.objects.count()
# передаем в шаблон в контенте
    return render(
        request,
        'index.html',
        context={'num_articles':num_articles,'num_authors':num_authors},
    )
# рендер оборачивает несколько вызовов в один и ищет файл куда будет вставялтся шаблон
def article_view(request):
    API_KEY=settings.ARTICLE_API_KEY
    query = request.GET.get('q', '')
    url = f"https://newsapi.org/v2/everything?q={query}&from=2026-01-21&language=kk&sortBy=popularity&apiKey={API_KEY}"

    response=requests.get(url)
    print("JSON ответа:", response.json())
    articles=response.json().get("articles",[])
    return render(
        request,
        'article.html',
        context={"articles":articles}
    )