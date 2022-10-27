from django.contrib import admin
from django.contrib.auth import admin as auth_admin
from django.contrib.auth.models import User

from .models import User

from .forms import (
    UserChangeForm,
    UserCreationForm,
)


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    form = UserChangeForm
    add_form = UserCreationForm
    fieldsets = (
        ('User', {'fields': ('discord_login', 'bio')}),
    ) + auth_admin.UserAdmin.fieldsets
    list_display = ['username', 'first_name', 'last_name', 'email', 'is_superuser', 'is_active']
    search_fields = ['username']
