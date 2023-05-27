# Django
from django.db import models

# Project
from apps.car.models import Car

class Image(models.Model):
    file = models.FileField(upload_to='media/images/%Y%M%d')
    car = models.ForeignKey(Car, on_delete=models.CASCADE)

    def __str__(self):
        return self.car.model.name

    class Meta:
        verbose_name = 'Image'
        verbose_name_plural = 'Images'
