from typing import ClassVar
from django.db import models

# Create your models here.
class Gif(models.Model):
    title = models.CharField(max_length=100)
    url = models.URLField()
    uploader_name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    likes = models.IntegerField(default=0)
    def __str__(self):
            return f'Gif {self.title}'

    @classmethod
    def get_liked_gifs(self):
        return self.objects.filter(likes__gte=0).order_by('-likes')


class Category(models.Model):
    category_name = models.CharField(max_length=100)
    gifs = models.ManyToManyField(Gif,related_name='categories')

    def __str__(self):
        return f'Category {self.category_name}'