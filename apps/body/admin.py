# Django
from django.contrib import admin

# Project
from apps.body.models import Body


@admin.register(Body)
class BodyAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_display_links = ['id', 'name']
    list_filter = ['name']
