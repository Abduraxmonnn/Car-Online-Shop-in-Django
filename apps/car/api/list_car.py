# Rest-Framework
from rest_framework.viewsets import ModelViewSet

# Project
from apps.car.models import Car
from apps.car.serializers import CarListSerializer


class CarListViewSet(ModelViewSet):
    queryset = Car.objects.all().select_related('model', 'color', 'transmission', 'body', 'created_by')
    serializer_class = CarListSerializer

