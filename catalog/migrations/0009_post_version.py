# Generated by Django 4.2.5 on 2023-10-29 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0008_alter_post_date_alter_product_date_of_creation_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='version',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Версия'),
        ),
    ]
