from django.contrib import admin
from .models import StartupCategory, Startup
from django import forms
from ckeditor.widgets import CKEditorWidget


class StartupAdmin(admin.ModelAdmin):
    content = forms.CharField(widget=CKEditorWidget())
    list_display = ['title']

    class Meta:
        model = Startup


class StartupCategoryAdmin(admin.ModelAdmin):
    list_display = ['name']


admin.site.register(Startup, StartupAdmin)
admin.site.register(StartupCategory, StartupCategoryAdmin)