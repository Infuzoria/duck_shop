# Generated by Django 4.2.5 on 2023-11-10 22:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mailing_app', '0003_newsletter_last_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='logs',
            name='date',
            field=models.CharField(verbose_name='Дата и время последней попытки'),
        ),
    ]
