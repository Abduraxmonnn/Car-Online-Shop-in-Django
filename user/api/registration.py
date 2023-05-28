# Rest-Framework
from rest_framework.views import APIView, Response
from rest_framework import status
from rest_framework.authtoken.models import Token

# Project
from user.models import User
from user.serializers.user import UserSignUpSerializer

class UserRegsitrationAPIView(APIView):
    model = User
    queryset = User.objects.order_by('-id').all()
    serializer_class = UserSignUpSerializer

    def post(self, request):
        serializer = UserSignUpSerializer(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)

        name = serializer.validated_data['fio']
        username = serializer.validated_data['username']
        age = serializer.validated_data['age']
        password = serializer.validated_data['password']
        is_admin = serializer.validated_data['is_admin']
        check_user = User.objects.filter(username__iexact=username)
        if check_user.exists():
            first = check_user.first()
            if first.otp is not None:
                if first.is_verified is True:
                    return Response({
                        "status_code": 400,
                        "message": "User exists",
                    }, status=status.HTTP_400_BAD_REQUEST)
                elif first.is_verified is False:
                    return Response({
                        "status_code": 400,
                        "message": "User is not Activate",
                    }, status=status.HTTP_400_BAD_REQUEST)

        user = User.objects.create_user(username=username, password=password)
        user.name = name
        user.username = username
        user.password = password
        user.age = age
        user.is_admin = is_admin
        user.is_active = True
        user.save()
        token = Token.objects.create(user=user)
        return Response({
            'status_code': 200,
            'message': 'Registration successfully check email',
            'token': token.key,
            'data': serializer.data
        }, status=status.HTTP_200_OK)
