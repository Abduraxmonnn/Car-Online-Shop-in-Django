# Django
from django.contrib import admin

# Project
from apps.car.models import Car
from apps.image.models import Image


class ImagePropertyInline(admin.TabularInline):
    model = Image
    extra = 3

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ['id', 'model', 'price', 'color', 'body', 'max_speed', 'is_sold']
    list_display_links = ['id', 'model', 'price', 'color']
    list_filter = ['model', 'color', 'body']
    search_fields = ['model', 'color', 'body']
    inlines = [ImagePropertyInline]
