from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True, verbose_name='Аватар пользователя')

    def __str__(self):
        return f'{self.username}'
    
    class Meta: 
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'