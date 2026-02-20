from django.db import models
from django.urls import reverse
from django.contrib import admin

class Author(models.Model):
    name=models.CharField(max_length=100)
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse("author_detail",args=[str(self.id)])

class Genre(models.Model):
    name=models.CharField(max_length=50)
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse("genre_detail",args=[str(self.id)])


class Articles(models.Model):
    title=models.CharField(max_length=200)
    description=models.TextField()
    content = models.TextField(default='')
    image=models.ImageField(upload_to='articles/', blank=True, null=True)
    release=models.DateTimeField(blank=True, null=True)
    author=models.ForeignKey("Author", on_delete=models.CASCADE)
    genre=models.ForeignKey("Genre", on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse("article_detail",args=[str(self.id)])
    
