# Django
from django.urls import path, include

# Project
from apps.basket.api import *

urlpatterns = [
    path('create/', BasketCreateAPIView.as_view()),
    # path('update/<int:pk>/', TransmissionUpdateAPIView.as_view()),
    # path('destroy/<int:pk>/', TransmissionDestroyAPIView.as_view()),
    # path('list/', CarListDetailViewSet.as_view({'get': 'list'})),
    path('my/<int:pk>/', MyBasketAPIView.as_view()),
]
