from django.contrib import admin
from .models import Technology, TechCategory


class TechnologyAdmin(admin.ModelAdmin):
    list_display = ['title']


class TechCategoryAdmin(admin.ModelAdmin):
    list_display = ['name']


admin.site.register(Technology, TechnologyAdmin)
admin.site.register(TechCategory, TechCategoryAdmin)