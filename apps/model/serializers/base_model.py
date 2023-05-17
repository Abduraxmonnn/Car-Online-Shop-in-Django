# Rest-Framework
from rest_framework import serializers

# Project
from apps.model.models import Model


class ModelBaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Model
        fields = '__all__'
