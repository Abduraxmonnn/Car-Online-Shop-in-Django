# Django
from django.urls import path, include

# Project
from apps.car.api import *

urlpatterns = [
    path('create/', CarCreateViewSet.as_view({'post': 'create'})),
    # path('update/<int:pk>/', TransmissionUpdateAPIView.as_view()),
    # path('destroy/<int:pk>/', TransmissionDestroyAPIView.as_view()),
    path('list/', CarListDetailViewSet.as_view({'get': 'list'})),
    path('detail/<int:pk>/', CarListDetailViewSet.as_view({'get': 'retrieve'})),
]
