from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=128)

    class Meta:
        db_table = ''
        verbose_name = 'Ff'
        verbose_name_plural = 'ff'