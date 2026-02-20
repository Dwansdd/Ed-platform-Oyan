from django.shortcuts import render

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

