# Generated by Django 4.2.5 on 2023-10-29 16:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0009_post_version'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='version',
        ),
    ]