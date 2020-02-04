from django.contrib import admin
from .models import PortfolioCategory, Portfolio
from django import forms
from ckeditor.widgets import CKEditorWidget


class PortfolioAdmin(admin.ModelAdmin):
    content = forms.CharField(widget=CKEditorWidget())
    list_display = ['title']

    class Meta:
        model = Portfolio


class PortfolioCategoryAdmin(admin.ModelAdmin):
    list_display = ['name']


admin.site.register(Portfolio, PortfolioAdmin)
admin.site.register(PortfolioCategory, PortfolioCategoryAdmin)