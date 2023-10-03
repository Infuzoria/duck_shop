from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='Наименование')
    description = models.CharField(max_length=800, verbose_name='Описание')
    image = models.ImageField(upload_to='catalog/', **NULLABLE, verbose_name='Фото')
    category = models.CharField(max_length=100, verbose_name='Категория')
    price = models.IntegerField(verbose_name='Цена')
    date_of_creation = models.DateField(**NULLABLE, verbose_name='Дата создания')
    last_modified_date = models.DateField(**NULLABLE, verbose_name='Дата последнего изменения')

    def __str__(self):
        return f'{self.name} ({self.category})'

    class Meta:
        verbose_name = 'товар'
        verbose_name_plural = 'товары'


class Category(models.Model):

    def __str__(self):
        pass

    class Meta:
        pass
