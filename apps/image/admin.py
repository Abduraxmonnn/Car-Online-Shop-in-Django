# Django
from django.contrib import admin
from django.utils.safestring import mark_safe

# Project
from apps.image.models import Image

@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ['id', 'render_image']

    def render_image(self, obj):
        return mark_safe("""<img src="/images/%s.jpg" />""" % obj.file)
