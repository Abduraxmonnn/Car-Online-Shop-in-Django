# Rest-Framework
from rest_framework import serializers

# Project
from apps.basket.models import Basket


class BasketUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Basket
        fields = [
            'id',
            'product',
            'quantity'
        ]
