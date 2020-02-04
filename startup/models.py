from django.db import models
from ckeditor.fields import RichTextField


class StartupCategory(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Startup(models.Model):
    title = models.CharField(max_length=100)
    category = models.ForeignKey(StartupCategory, on_delete=models.CASCADE)
    thumbnail = models.ImageField()
    content = RichTextField()
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title
