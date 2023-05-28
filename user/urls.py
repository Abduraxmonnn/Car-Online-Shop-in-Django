# Django
from django.urls import path

# Project
from user.api import UserRegsitrationAPIView, UserLogInView, UserTokenAPIView, UserListView, UserDeleteAPIView, \
    UserMeView

urlpatterns = [
    path('registration/', UserRegsitrationAPIView.as_view()),
    path('signin/', UserLogInView.as_view()),
    path('token/get/<int:pk>/', UserTokenAPIView.as_view()),
    path('list/<int:is_admin>/', UserListView.as_view()),
    path('me/', UserMeView.as_view()),
    path('me/<int:pk>/', UserMeView.as_view()),
    path('delete/<int:pk>/', UserDeleteAPIView.as_view()),
]
