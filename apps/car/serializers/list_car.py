# Rest-Framework
from rest_framework import serializers

# Project
from apps.car.models import Car
from apps.body.serializers import BodyBaseSerializer
from apps.color.serializers import ColorBaseSerializer
from apps.model.serializers import ModelBaseSerializer
from apps.transmission.serializers import TransmissionBaseSerializer
from user.models import User

class CarUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'age',
            'is_admin'
        ]

class CarListSerializer(serializers.ModelSerializer):
    model = ModelBaseSerializer()
    color = ColorBaseSerializer()
    transmission = TransmissionBaseSerializer()
    body = BodyBaseSerializer()
    created_by = CarUserSerializer()

    class Meta:
        model = Car
        fields = [
            'id',
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
            'created_by',
            'created_date',
            'last_updated'
        ]
