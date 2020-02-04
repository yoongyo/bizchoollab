from django.contrib import admin
from .models import Technology, TechCategory
from django import forms
from ckeditor.widgets import CKEditorWidget


class TechnologyAdmin(admin.ModelAdmin):
    content = forms.CharField(widget=CKEditorWidget())
    list_display = ['title']

    class Meta:
        model = Technology



class TechCategoryAdmin(admin.ModelAdmin):
    list_display = ['name']


admin.site.register(Technology, TechnologyAdmin)
admin.site.register(TechCategory, TechCategoryAdmin)