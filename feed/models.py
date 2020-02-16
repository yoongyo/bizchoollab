from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.conf import settings


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
    admin = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    childCategory = models.ForeignKey(ChildCategory, on_delete=models.CASCADE)
    thumbnail = models.ImageField(blank=True, null=True)
    content = RichTextUploadingField(blank=True,
                                     null=True,
                                     external_plugin_resources=[(
                                         'youtube',
                                         '/static/base/vendor/ckeditor_plugins/youtube/youtube/',
                                         'plugin.js',
                                     )])

    created_at = models.DateField(auto_now_add=True)
    tag = models.ManyToManyField(Tag, related_name="tag", blank=True)

    def __str__(self):
        return self.title