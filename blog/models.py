from django.db import models
import datetime

NULLABLE = {'blank': True, 'null': True}


class Post(models.Model):
    title = models.CharField(max_length=100, verbose_name='Заголовок')
    slug = models.CharField(max_length=100, verbose_name='slug')
    text = models.CharField(max_length=2000, verbose_name='Содержимое')
    image = models.ImageField(upload_to='catalog/', **NULLABLE, verbose_name='Превью')
    date = models.DateField(default=datetime.date.today, verbose_name='Дата создания')
    is_published = models.BooleanField(default=True, verbose_name='Признак публикации')
    views_count = models.IntegerField(default=0, verbose_name='Количество просмотров')

    def __str__(self):
        return f'{self.title} ({self.slug})'

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
