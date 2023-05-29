# Rest-Framework
from rest_framework import serializers

# Project
from apps.basket.models import Basket


class BasketCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Basket
        fields = [
            'id',
            'product',
            'quantity'
        ]
