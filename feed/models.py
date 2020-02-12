from django.db import models
from ckeditor.fields import RichTextField


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class ChildCategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Feed(models.Model):
    title = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    childCategory = models.ForeignKey(ChildCategory, on_delete=models.CASCADE)
    thumbnail = models.ImageField(blank=True, null=True)
    content = RichTextField()
    created_at = models.DateField(auto_now_add=True)
    tag = models.ManyToManyField(Tag, related_name="tag", blank=True)

    def __str__(self):
        return self.title