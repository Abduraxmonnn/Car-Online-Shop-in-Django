# Django
from django.db import models

# Project
from apps.car.models import Car
from user.models import User


class Basket(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    product = models.ForeignKey(to=Car, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Basket for {self.user.username} and Product {self.product.model.name}'

    class Meta:
        verbose_name = 'Basket'
        verbose_name_plural = 'Baskets'
