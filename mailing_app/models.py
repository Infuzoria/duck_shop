from django.db import models


class Client(models.Model):
    email = models.CharField(max_length=100, verbose_name='Email пользователя')
    name = models.CharField(max_length=100, verbose_name='ФИО пользователя')
    text = models.TextField(verbose_name='Комментарий')

    def __str__(self):
        return f'{self.name} ({self.email})'

    class Meta:
        verbose_name = 'клиент'
        verbose_name_plural = 'клиенты'
