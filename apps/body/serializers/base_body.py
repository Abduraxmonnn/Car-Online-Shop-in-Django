# Rest-Framework
from rest_framework import serializers

# Project
from apps.body.models import Body

class BodyBaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Body
        fields = [
            'id',
            'name'
        ]
