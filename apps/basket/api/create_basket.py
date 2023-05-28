# Rest-Framework
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

# Project
from apps.basket.models import Basket
from apps.basket.serializers import BasketCreateSerializer


class BasketCreateAPIView(APIView):
    model = Basket
    queryset = Basket.objects.order_by('-id').all()
    serializer_class = BasketCreateSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)

        user = request.user
        product = serializer.validated_data['product']
        quantity = serializer.validated_data['quantity']
        check_basket = Basket.objects.filter(user=user, product=product)

        if not check_basket.exists():
            basket = Basket.objects.create(user=user, product=product)
            basket.total_price = product.price * quantity
            basket.save()
        else:
            basket = check_basket.first()
            basket.quantity += 1
            basket.total_price = product.price * quantity
            basket.save()

        return Response({
            'status': 'Successfully',
            'product_brand': product.model.brand.name,
            'product_model': product.model.name,
            'product_price': product.price,
            "quantity": quantity,
            "total_price": float(basket.total_price)
        }, status=status.HTTP_200_OK)
