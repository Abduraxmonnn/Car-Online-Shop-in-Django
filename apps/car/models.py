# Django
from django.db import models

# Project
from apps.model.models import Model
from apps.color.models import Color
from apps.transmission.models import Transmission
from apps.body.models import Body
from user.models import User

class Car(models.Model):
    model = models.ForeignKey(Model, on_delete=models.CASCADE)
    description = models.TextField()
    price = models.FloatField()
    color = models.ForeignKey(Color, on_delete=models.CASCADE)
    transmission = models.ForeignKey(Transmission, on_delete=models.CASCADE)
    body = models.ForeignKey(Body, on_delete=models.CASCADE)
    max_speed = models.IntegerField()
    is_sold = models.BooleanField(default=False)
    is_public = models.BooleanField(default=False)
    engine = models.FloatField()
    year = models.IntegerField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.model.name} {self.price} {self.color}'

    class Meta:
        verbose_name = 'Car'
        verbose_name_plural = 'Cars'
