# Rest-Framework
from rest_framework import serializers

# Project
from apps.basket.models import Basket


class BasketBaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Basket
        fields = '__all__'
