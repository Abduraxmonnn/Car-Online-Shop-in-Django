
# Rest-Framework
from rest_framework import viewsets

# Project
from apps.car.models import Car
from apps.car.serializers import CarCreateSerializer


class CarCreateViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarCreateSerializer
    http_method_names = ['post']
