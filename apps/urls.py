# Django
from django.urls import path, include
from rest_framework import routers

# Project
from apps.brand.api import BrandBaseViewSet
from apps.model.api import ModelBaseViewSet
from apps.color.api import ColorBaseViewSet


router = routers.DefaultRouter()
router.register(r'brand', BrandBaseViewSet)
router.register(r'model', ModelBaseViewSet)
router.register(r'color', ColorBaseViewSet)

urlpatterns = [
    path('', include(router.urls))
]
