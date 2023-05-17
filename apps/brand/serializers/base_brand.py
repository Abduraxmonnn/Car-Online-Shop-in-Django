# Rest-Framework
from rest_framework import serializers

# Project
from apps.brand.models import Brand


class BrandBaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'
