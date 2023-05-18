# Django
from django.db import models


class Transmission(models.Model):
    type = models.CharField(max_length=155)

    def __str__(self):
        return self.type

    class Meta:
        verbose_name = 'Transmission'
        verbose_name_plural = 'Transmissions'
