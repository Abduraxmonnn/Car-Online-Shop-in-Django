# Django
from django.urls import path, include
from rest_framework import routers

# Project
from apps.brand.api import BrandBaseViewSet
from apps.model.api import ModelBaseViewSet
from apps.color.api import ColorBaseViewSet
from apps.body.api import BodyBaseViewSet


router = routers.DefaultRouter()
router.register(r'brand', BrandBaseViewSet)
router.register(r'model', ModelBaseViewSet)
router.register(r'color', ColorBaseViewSet)
router.register(r'body', BodyBaseViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('transmission/', include('apps.transmission.urls')),
]
