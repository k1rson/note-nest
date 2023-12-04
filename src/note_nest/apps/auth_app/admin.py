from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'is_staff', 'get_groups_display')  # Используем get_groups_display
    search_fields = ('username', 'email')
    list_filter = ('is_staff', 'groups')  # Используем 'groups' вместо 'group'

    fieldsets = (
        (None, {'fields': ('username', 'email', 'password', 'avatar')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions', 'is_enabled_email_auth', 'is_enabled_telegram_auth')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2', 'is_active', 'is_staff', 'is_superuser', 'groups'),
        }),
    )

    def get_groups_display(self, obj):
        return ", ".join([group.name for group in obj.groups.all()])

admin.site.register(CustomUser, CustomUserAdmin)
