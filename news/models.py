from django.db import models


class Media(models.Model):
    name = models.CharField(max_length=255, unique=True)
    title_rule = models.CharField(max_length=255)
    url = models.URLField()


class Article(models.Model):
    media = models.ForeignKey(to=Media, on_delete=models.CASCADE)
    title = models.TextField()
    url = models.TextField(unique=True)
    date = models.DateTimeField()
