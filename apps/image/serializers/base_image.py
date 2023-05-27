# Rest-Framework
from rest_framework import serializers

# Project
from apps.image.models import Image

class ImageBaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = [
            'id',
            'file',
            'car'
        ]
