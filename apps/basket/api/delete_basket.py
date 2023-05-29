# Django
from django.shortcuts import get_object_or_404

# Rest-Framework
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

# Project
from apps.basket.models import Basket
from apps.basket.serializers import BasketBaseSerializer


class BasketDeleteAPIView(APIView):
    model = Basket
    queryset = Basket.objects.order_by('-id').all()
    serializer_class = BasketBaseSerializer
    permission_classes = [IsAuthenticated]

    def delete(self, request, pk=None):
        basket = get_object_or_404(self.queryset, pk=pk)
        serializer = self.serializer_class(basket)
        if request.user == basket.user:
            basket.delete()
            return Response({
                'message': 'Product Deleted Successfully',
                'product_brand': basket.product.model.brand.name,
                'product_model': basket.product.model.name,
                'product_price': basket.product.price,
                'quantity': basket.quantity,
                'total_price': float(basket.total_price)
            }, status=status.HTTP_200_OK)
        else:
            return Response({
                'message': 'Error You do not have permission for delete others basket',
                'product_data': serializer.data
            }, status=status.HTTP_400_BAD_REQUEST)
