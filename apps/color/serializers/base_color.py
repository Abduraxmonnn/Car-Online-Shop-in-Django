# Rest-Framework
from rest_framework import serializers

# Project
from apps.color.models import Color


class ColorBaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = '__all__'
