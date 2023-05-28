# Django
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models

# Project
from user.manager import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    fio = models.CharField(max_length=255)
    username = models.CharField(max_length=150, unique=True)
    age = models.IntegerField(null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    last_login = models.DateTimeField(blank=True, null=True)

    objects = UserManager()

    USERNAME_FIELD = 'username'

    def __str__(self):
        return f'{self.username} {self.age}'

    @property
    def is_staff(self):
        return self.is_admin

    def is_member(self, *groups):
        """
        This method used to check group of user.
        If result will be True then User member of this group otherwise not member
        :return: boolean
        """
        return self.groups.filter(name__in=groups).exists()

    @property
    def dob(self):
        import datetime
        return int(datetime.date.today().year - self.age)

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
        ordering = ['username']
