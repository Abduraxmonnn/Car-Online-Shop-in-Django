# Django
from django.contrib.auth import authenticate, login

# Rest-Framework
from rest_framework import status
from rest_framework.authtoken.views import APIView
from rest_framework.response import Response

# Project
from user.serializers.user import UserLogInSerializer
from user.models import User


class UserLogInView(APIView):
    model = User
    queryset = User.objects.order_by('-id').all()
    serializer_class = UserLogInSerializer

    def post(self, request):
        serializer = UserLogInSerializer(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        username = serializer.validated_data['username']
        password = serializer.validated_data['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                    login(request, user=user)

                    return Response({
                        'status_code': 200,
                        'message': 'Successfully'
                    }, status=status.HTTP_200_OK)
            else:
                return Response({
                    'status_code': 404,
                    'message': 'User is not active'
                }, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({
                'status_code': 404,
                'message': 'User does not exists (None)'
            })
