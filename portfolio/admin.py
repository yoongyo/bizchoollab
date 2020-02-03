from django.contrib import admin
from .models import PortfolioCategory, Portfolio


class PortfolioAdmin(admin.ModelAdmin):
    list_display = ['title']


class PortfolioCategoryAdmin(admin.ModelAdmin):
    list_display = ['name']


admin.site.register(Portfolio, PortfolioAdmin)
admin.site.register(PortfolioCategory, PortfolioCategoryAdmin)