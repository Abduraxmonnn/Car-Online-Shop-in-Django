# Django
from django_filters.rest_framework import DjangoFilterBackend

# Rest-Framework
from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

# Project
from apps.image.serializers import ImageBaseSerializer
from apps.image.models import Image


class ImageBaseViewSet(mixins.CreateModelMixin,
                       mixins.RetrieveModelMixin,
                       mixins.UpdateModelMixin,
                       mixins.DestroyModelMixin,
                       mixins.ListModelMixin,
                       GenericViewSet):

    queryset = Image.objects.all()
    serializer_class = ImageBaseSerializer
