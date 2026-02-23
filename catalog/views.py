from django.shortcuts import render
import requests
from django.conf import settings
from .models import Articles, Author, Genre
from django.http import JsonResponse
from catalog.models import Articles
from catalog.serializers.article import ArticleSerializer
from django.views.generic.detail import DetailView
from django.views import generic
# прописываем логику в обьект request 
def index(request):
    num_articles=Articles.objects.all().count()
    num_authors=Author.objects.count()
    articles=Articles.objects.all().count()
# передаем в шаблон в контенте
    return render(
        request,
        'index.html',
        context={'num_articles':num_articles,'num_authors':num_authors},
    )

# рендер оборачивает несколько вызовов в один и ищет файл куда будет вставялтся шаблон
def article_view_api(request):
    # API_KEY=settings.ARTICLE_API_KEY
    # query = request.GET.get('q', '')
    articles = [
        "Алматы",
        "Астана",
        "Қазақстан",
        "Шымкент"
    ]
    headers = {"User-Agent": "MyKazakhApp/1.0 (example@example.com)"}
    for title in articles:
        url = f"https://kk.wikipedia.org/api/rest_v1/page/summary/{title}"
        response=requests.get(url,headers=headers)
        wiki_data = response.json()
        
        data = {
            "title": wiki_data.get("title"),
            "description": wiki_data.get("extract"),
            "content": wiki_data.get("extract"),
            "image": wiki_data.get("thumbnail", {}).get("source"),
            "source_url": wiki_data.get("content_urls", {})
                    .get("desktop", {})
                    .get("page"),
}
        if response.status_code==200:
            data=response.json()
            serializer=ArticleSerializer(data=data)
            if  serializer.is_valid():
                serializer.save()


class archive_articleslist(generic.ListView):
    model=Articles
    template_name = 'article.html'
# def archive_articleslist(request):
#     articles=Articles.objects.all()
#     return render(
#         request,
#         'article.html',
#         context={'archive_articleslist':articles},
    # )

# class ArticleDetailView(DetailView):
#     model = Articles

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context["now"] = timezone.now()
#         return context