# Django
from django_filters.rest_framework import DjangoFilterBackend

# Rest-Framework
from rest_framework import viewsets
from rest_framework.filters import SearchFilter, OrderingFilter

# Project
from apps.body.models import Body
from apps.body.serializers import BodyBaseSerializer


class BodyBaseViewSet(viewsets.ModelViewSet):
    queryset = Body.objects.all()
    serializer_class = BodyBaseSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = [
        'name',
    ]
    search_fields = [
        '^name',
    ]
    ordering_fields = ['name', '-id']
    ordering = ['-id']
