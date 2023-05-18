# Django
from django.contrib import admin

# Project
from user.models import User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'age', 'is_admin', 'is_active', 'last_login']
    list_display_links = ['id', 'username', 'age']
    list_filter = ['username', 'age', 'is_admin', 'is_active']
