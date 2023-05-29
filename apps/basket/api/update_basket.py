# Django
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response

# Rest-Framework
from rest_framework.views import APIView

# Project
from apps.basket.models import Basket
from apps.basket.serializers import BasketUpdateSerializer


class BasketUpdateAPIView(APIView):
    model = Basket
    queryset = Basket.objects.order_by('-id').all()
    serializer_class = BasketUpdateSerializer

    def put(self, request, pk=None):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)

        basket = get_object_or_404(self.model, pk=pk)
        quantity = serializer.validated_data['quantity']

        if request.user == basket.user:
            basket = self.model.objects.first()
            basket.quantity = quantity
            basket.total_price = basket.product.price * quantity
            basket.save()
            return Response({
                'message': 'Product Updated Successfully',
                'product_brand': basket.product.model.brand.name,
                'product_model': basket.product.model.name,
                'product_price': basket.product.price,
                'quantity': basket.quantity,
                'total_price': float(basket.total_price)
            }, status=status.HTTP_200_OK)
        else:
            return Response({
                'Error': 'You are not owner of Basket'
            }, status=status.HTTP_400_BAD_REQUEST)
