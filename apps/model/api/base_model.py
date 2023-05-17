# Django
from django_filters.rest_framework import DjangoFilterBackend

# Rest-Framework
from rest_framework import mixins, viewsets
from rest_framework.filters import SearchFilter, OrderingFilter

# Project
from apps.model.models import Model
from apps.model.serializers import ModelBaseSerializer


class ModelBaseViewSet(mixins.CreateModelMixin,
                       mixins.RetrieveModelMixin,
                       mixins.UpdateModelMixin,
                       mixins.DestroyModelMixin,
                       mixins.ListModelMixin,
                       viewsets.GenericViewSet):
    queryset = Model.objects.all()
    serializer_class = ModelBaseSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = [
        'name',

        'brand__name',
    ]
    search_fields = [
        'name',

        'brand__name',
    ]
    ordering_fields = ['name', '-id']
    ordering = ['-id']
