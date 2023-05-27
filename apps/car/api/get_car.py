# Django
from django_filters.rest_framework import DjangoFilterBackend

# Rest-Framework
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter, OrderingFilter

# Project
from apps.car.models import Car
from apps.car.serializers import CarListDetailSerializer
from apps.custom_filters import CarFilter


class CarListDetailViewSet(ModelViewSet):
    queryset = Car.objects.all().select_related('model', 'color', 'transmission', 'body', 'created_by')
    serializer_class = CarListDetailSerializer
    permission_classes = [AllowAny]
    http_method_names = ['get']

    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = CarFilter
    search_fields = [
        '^model__name',
        'brand__name',
        'body__name',
    ]
    ordering_fields = ['id', 'max_speed', 'engine', 'year']
    ordering = ['-id']
