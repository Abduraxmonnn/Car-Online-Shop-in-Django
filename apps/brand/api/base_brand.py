# Django
from django_filters.rest_framework import DjangoFilterBackend

# Rest-Framework
from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet
from rest_framework.filters import SearchFilter, OrderingFilter

# Project
from ..serializers import BrandBaseSerializer
from ..models import Brand


class BrandBaseViewSet(mixins.CreateModelMixin,
                       mixins.RetrieveModelMixin,
                       mixins.UpdateModelMixin,
                       mixins.DestroyModelMixin,
                       mixins.ListModelMixin,
                       GenericViewSet):

    queryset = Brand.objects.all()
    serializer_class = BrandBaseSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = [
        'name',
    ]
    search_fields = [
        '^name',
    ]
    ordering_fields = ['name', '-id']
    ordering = ['-id']
