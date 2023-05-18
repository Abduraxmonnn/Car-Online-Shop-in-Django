# Rest-Framework
from rest_framework import serializers

# Project
from apps.transmission.models import Transmission


class TransmissionBaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transmission
        fields = [
            'id',
            'type',
        ]
