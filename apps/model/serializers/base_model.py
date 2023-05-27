# Rest-Framework
from rest_framework import serializers

# Project
from apps.model.models import Model
from apps.brand.serializers import BrandBaseSerializer


class ModelBaseSerializer(serializers.ModelSerializer):
    brand = BrandBaseSerializer()

    class Meta:
        model = Model
        fields = [
            'id',
            'name',
            'brand'
        ]
