# Django
from django_filters.rest_framework import DjangoFilterBackend

# Rest-Framework
from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet
from rest_framework.filters import SearchFilter, OrderingFilter

# Project
from apps.color.serializers import ColorBaseSerializer
from apps.color.models import Color


class ColorBaseViewSet(mixins.CreateModelMixin,
                       mixins.RetrieveModelMixin,
                       mixins.UpdateModelMixin,
                       mixins.DestroyModelMixin,
                       mixins.ListModelMixin,
                       GenericViewSet):

    queryset = Color.objects.all()
    serializer_class = ColorBaseSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = [
        'name',
    ]
    search_fields = [
        '^name',
    ]
    ordering_fields = ['name', '-id']
    ordering = ['-id']
