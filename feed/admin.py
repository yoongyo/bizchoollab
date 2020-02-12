from django.contrib import admin
from .models import Feed, Category, Tag, ChildCategory


class FeedAdmin(admin.ModelAdmin):
    list_display = ['title']


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']


class TagAdmin(admin.ModelAdmin):
    list_display = ['name']


class ChildCategoryAdmin(admin.ModelAdmin):
    list_display = ['name']


admin.site.register(Feed, FeedAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(ChildCategory, ChildCategoryAdmin)