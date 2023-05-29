# Django
from django.urls import path, include

# Project
from apps.basket.api import *

urlpatterns = [
    path('create/', BasketCreateAPIView.as_view()),
    path('update/<int:pk>/', BasketUpdateAPIView.as_view()),
    path('delete/<int:pk>/', BasketDeleteAPIView.as_view()),
    path('my/<int:pk>/', MyBasketAPIView.as_view()),
]
