# Django
from django.shortcuts import get_object_or_404

# Rest-Framework
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

# Project
from apps.basket.models import Basket
from apps.basket.serializers import MyBasketSerializer

class MyBasketAPIView(APIView):
    model = Basket
    queryset = Basket.objects.order_by('-id').all()
    serializer_class = MyBasketSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request, pk=None):
        queryset = Basket.objects.all()
        basket = get_object_or_404(queryset, pk=pk)
        serializer = MyBasketSerializer(basket)
        if basket.user == request.user or request.user.is_admin is True:
            return Response({
                'message': 'Successfully',
                'product_brand': basket.product.model.brand.name,
                'product_model': basket.product.model.name,
                'product_price': basket.product.price,
                'quantity': basket.quantity,
                'total_price': float(basket.total_price),
                'product_data': serializer.data,
            }, status=status.HTTP_200_OK)
        else:
            return Response({
                'Error': 'You are not owner of Basket'
            }, status=status.HTTP_400_BAD_REQUEST)
