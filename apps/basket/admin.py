# Django
from django.contrib import admin

# Project
from apps.basket.models import Basket


@admin.register(Basket)
class BasketAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'product', 'get_product_id']
    list_display_links = ['id', 'user']

    def get_product_id(self, obj):
        return obj.product.id
