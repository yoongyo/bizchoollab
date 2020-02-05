from django.contrib import admin
from .models import Peed, Category, Tag


class PeedAdmin(admin.ModelAdmin):
    list_display = ['title']


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']


class TagAdmin(admin.ModelAdmin):
    list_display = ['name']


admin.site.register(Peed, PeedAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)
