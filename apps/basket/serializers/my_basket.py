# Rest-Framework
from rest_framework import serializers

# Project
from apps.basket.models import Basket
from apps.car.serializers import CarListDetailSerializer


class MyBasketSerializer(serializers.ModelSerializer):
    product = CarListDetailSerializer()

    class Meta:
        model = Basket
        fields = [
            'id',
            'product',
            'quantity'
        ]
