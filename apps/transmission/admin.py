# Django
from django.contrib import admin

# Project
from apps.transmission.models import Transmission


@admin.register(Transmission)
class TransmissionAdmin(admin.ModelAdmin):
    list_display = ['id', 'type']
    list_display_links = ['id', 'type']
    list_filter = ['type']
