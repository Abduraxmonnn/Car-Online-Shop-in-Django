# Django
from django.db import models

# Project
from apps.brand.models import Brand

class Model(models.Model):
    name = models.CharField(max_length=255)
    brand = models.ForeignKey(Brand, on_delete=Brand)

    def __str__(self):
        return f'{self.name}, {self.brand.name}'

    class Meta:
        verbose_name = 'Model'
        verbose_name_plural = 'Models'
