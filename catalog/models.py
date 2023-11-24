from django.db import models
import datetime

NULLABLE = {'blank': True, 'null': True}


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Наименование')
    description = models.CharField(max_length=800, verbose_name='Описание')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='Наименование')
    description = models.CharField(max_length=2000, verbose_name='Описание')
    image = models.ImageField(upload_to='catalog/', **NULLABLE, verbose_name='Фото')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
    price = models.IntegerField(verbose_name='Цена')
    date_of_creation = models.DateField(default=datetime.date.today, verbose_name='Дата создания')
    last_modified_date = models.DateField(default=datetime.date.today, verbose_name='Дата последнего изменения')
    active_version = models.CharField(max_length=100, **NULLABLE, verbose_name='Версия')

    def __str__(self):
        return f'{self.name} ({self.category})'

    class Meta:
        verbose_name = 'товар'
        verbose_name_plural = 'товары'


class Request(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя пользователя')
    email = models.CharField(max_length=100, verbose_name='Email пользователя')
    message = models.CharField(max_length=500, verbose_name='Сообщение')

    def __str__(self):
        return f'{self.name} ({self.email})'

    class Meta:
        verbose_name = 'Ответ'
        verbose_name_plural = 'Ответы'


class Version(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Продукт')
    version_number = models.CharField(max_length=15, verbose_name='Номер версии')
    version_name = models.CharField(max_length=100, verbose_name='Название версии')
    is_active = models.BooleanField(default=True, verbose_name='Признак версии')

    def __str__(self):
        return f'{self.version_number} ({self.version_name})'

    class Meta:
        verbose_name = 'Версия'
        verbose_name_plural = 'Версии'
