from django.db import models
from users.models import User

NULLABLE = {'blank': True, 'null': True}


class Client(models.Model):
    email = models.CharField(max_length=100, verbose_name='Email пользователя')
    name = models.CharField(max_length=100, verbose_name='ФИО пользователя')
    text = models.TextField(verbose_name='Комментарий')
    owner_id = models.ForeignKey(User, **NULLABLE, on_delete=models.CASCADE, verbose_name='id создателя')

    def __str__(self):
        return f'{self.name} ({self.email})'

    class Meta:
        verbose_name = 'клиент'
        verbose_name_plural = 'клиенты'


class Text(models.Model):
    topic = models.CharField(max_length=100, verbose_name='Тема письма')
    text = models.TextField(verbose_name='Тело письма')

    def __str__(self):
        return f'{self.text}'

    class Meta:
        verbose_name = 'сообщение'
        verbose_name_plural = 'сообщения'


class Newsletter(models.Model):

    PERIODICITY = (
        ('day', 'Один раз в день'),
        ('week', 'Один раз в неделю'),
        ('month', 'Один раз в месяц'),
    )

    STATUS = (
        ('completed', 'Завершена'),
        ('created', 'Создана'),
        ('launched', 'Запущена'),
    )

    start_time = models.CharField(verbose_name='Время начала рассылки')
    stop_time = models.CharField(verbose_name='Время окончания рассылки')
    last_time = models.CharField(**NULLABLE, verbose_name='Время последней рассылки')
    period = models.CharField(max_length=100, choices=PERIODICITY, verbose_name=' Периодичность рассылки')
    status = models.CharField(default='created', max_length=20, choices=STATUS, verbose_name='Статус рассылки')
    message = models.ForeignKey(Text, on_delete=models.CASCADE, verbose_name='Текст рассылки')
    client = models.ManyToManyField(Client)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, **NULLABLE, verbose_name='Создатель рассылки')
    is_active = models.BooleanField(default=True, verbose_name='Признак активности')

    def __str__(self):
        return f'{self.start_time} {self.period} {self.status}'

    class Meta:
        verbose_name = 'рассылка'
        verbose_name_plural = 'рассылки'


class Logs(models.Model):
    date = models.CharField(verbose_name='Дата и время последней попытки')
    status = models.BooleanField(verbose_name='Статус рассылки')
    error_msg = models.CharField(default='None', max_length=300, verbose_name='Ответ почтового сервера')
    client = models.ForeignKey(Client, on_delete=models.CASCADE, verbose_name='Пользователь')
    newsletter = models.ForeignKey(Newsletter, on_delete=models.CASCADE, verbose_name='Рассылка')

    def __str__(self):
        return f'{self.date} {self.status} ({self.error_msg})'

    class Meta:
        verbose_name = 'лог'
        verbose_name_plural = 'логи'
