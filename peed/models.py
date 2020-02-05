from django.db import models
from ckeditor.fields import RichTextField


class Category(models.Model):
    name = models.CharField(max_length=100)


class Tag(models.Model):
    name = models.CharField(max_length=100)


class Peed(models.Model):
    title = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    thumbnail = models.ImageField()
    content = RichTextField()
    created_at = models.DateField(auto_now_add=True)
    tag = models.ManyToManyField(Tag, related_name="tag")

    def __str__(self):
        return self.title