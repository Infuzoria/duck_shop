from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {'blank': True, 'null': True}


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='Почта')
    phone = models.CharField(max_length=20, verbose_name='Телефон', **NULLABLE)
    avatar = models.ImageField(upload_to='catalog/', **NULLABLE, verbose_name='Фото')
    is_active = models.BooleanField(default=True, verbose_name='Признак активности')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

