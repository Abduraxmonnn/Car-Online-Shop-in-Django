# Django
from django.contrib import admin

# Project
from apps.model.models import Model


@admin.register(Model)
class ModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_display_links = ['id', 'name']
    list_filter = ['name']
