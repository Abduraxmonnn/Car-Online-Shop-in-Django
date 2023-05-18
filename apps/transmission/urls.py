# Django
from django.urls import path, include

# Project
from apps.transmission.api import *

urlpatterns = [
    path('create/', TransmissionCreateAPIView.as_view()),
    path('update/<int:pk>/', TransmissionUpdateAPIView.as_view()),
    path('destroy/<int:pk>/', TransmissionDestroyAPIView.as_view()),
    path('list/', TransmissionListAPIVIew.as_view()),
    path('detail/<int:pk>/', TransmissionRetrieveAPIVIew.as_view()),
]
