from django.contrib import admin
from .models import NewsCategory, News


class NewsAdmin(admin.ModelAdmin):
    list_display = ['title']


class NewsCategoryAdmin(admin.ModelAdmin):
    list_display = ['name']


admin.site.register(News, NewsAdmin)
admin.site.register(NewsCategory, NewsCategoryAdmin)