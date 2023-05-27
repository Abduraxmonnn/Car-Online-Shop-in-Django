# Django
from django.urls import path, include
from rest_framework import routers

# Project
from apps.brand.api import BrandBaseViewSet
from apps.model.api import ModelBaseViewSet
from apps.color.api import ColorBaseViewSet
from apps.body.api import BodyBaseViewSet
from apps.image.api import ImageBaseViewSet


router = routers.DefaultRouter()
router.register(r'brand', BrandBaseViewSet)
router.register(r'model', ModelBaseViewSet)
router.register(r'color', ColorBaseViewSet)
router.register(r'body', BodyBaseViewSet)
router.register(r'image', ImageBaseViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('transmission/', include('apps.transmission.urls')),
    path('car/', include('apps.car.urls')),
]
