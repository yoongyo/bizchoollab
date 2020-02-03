from django.contrib import admin
from .models import StartupCategory, Startup


class StartupAdmin(admin.ModelAdmin):
    list_display = ['title']


class StartupCategoryAdmin(admin.ModelAdmin):
    list_display = ['name']


admin.site.register(Startup, StartupAdmin)
admin.site.register(StartupCategory, StartupCategoryAdmin)