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


class Newsletter(models.Model):
    time = models.DateField(verbose_name='Время рассылки')
    period = models.CharField(max_length=100, verbose_name=' Периодичность рассылки')
    status = models.CharField(default='created', max_length=20, verbose_name='Статус рассылки')

    def __str__(self):
        return f'{self.time} {self.period} {self.status}'

    class Meta:
        verbose_name = 'рассылка'
        verbose_name_plural = 'рассылки'
