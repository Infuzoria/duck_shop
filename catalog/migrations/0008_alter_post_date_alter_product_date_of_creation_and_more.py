# Generated by Django 4.2.5 on 2023-10-29 03:28

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0007_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date',
            field=models.DateField(default=datetime.date.today, verbose_name='Дата создания'),
        ),
        migrations.AlterField(
            model_name='product',
            name='date_of_creation',
            field=models.DateField(default=datetime.date.today, verbose_name='Дата создания'),
        ),
        migrations.AlterField(
            model_name='product',
            name='last_modified_date',
            field=models.DateField(default=datetime.date.today, verbose_name='Дата последнего изменения'),
        ),
        migrations.CreateModel(
            name='Version',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('version_number', models.CharField(max_length=15, verbose_name='Номер версии')),
                ('version_name', models.CharField(max_length=100, verbose_name='Название версии')),
                ('is_active', models.BooleanField(default=True, verbose_name='Признак версии')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.product', verbose_name='Продукт')),
            ],
            options={
                'verbose_name': 'Версия',
                'verbose_name_plural': 'Версии',
            },
        ),
    ]
