from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True, verbose_name='Аватар пользователя')
    is_enabled_email_auth = models.BooleanField(default=False, verbose_name='Аутентификация через Email')
    is_enabled_telegram_auth = models.BooleanField(default=False, verbose_name='Аутентификация через Telegram бота')

    def __str__(self):
        return f'{self.username}'
    
    class Meta: 
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'