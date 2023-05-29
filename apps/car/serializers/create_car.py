# Rest-Framework
from rest_framework import serializers

# Project
from apps.car.models import Car


class CarCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = [
            'model',
            'description',
            'price',
            'color',
            'transmission',
            'body',
            'max_speed',
            'is_sold',
            'is_public',
            'engine',
            'year',
            'created_by'
        ]
