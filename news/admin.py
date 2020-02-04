from django.contrib import admin
from .models import NewsCategory, News
from django import forms
from ckeditor.widgets import CKEditorWidget


class NewsAdmin(admin.ModelAdmin):
    content = forms.CharField(widget=CKEditorWidget())
    list_display = ['title']

    class Meta:
        model = News


class NewsCategoryAdmin(admin.ModelAdmin):
    list_display = ['name']


admin.site.register(News, NewsAdmin)
admin.site.register(NewsCategory, NewsCategoryAdmin)