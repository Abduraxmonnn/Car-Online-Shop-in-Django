# Django
from django.db import models


class Body(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Body'
        verbose_name_plural = 'Bodies'
