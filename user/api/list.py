# Rest-Framework
from rest_framework.response import Response
from rest_framework.viewsets import mixins
from rest_framework import viewsets, views
from rest_framework.permissions import IsAdminUser, AllowAny

# Project
from user.models import User
from user.serializers.user import UserSerializer

class UserListView(views.APIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

    def get(self, request, is_admin=False):

        if is_admin == 0:
            queryset = User.objects.filter(is_admin=False)
        else:
            queryset = User.objects.filter(is_admin=True)
        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data)
