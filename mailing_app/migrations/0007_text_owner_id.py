# Generated by Django 4.2.5 on 2023-11-19 08:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mailing_app', '0006_client_owner_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='text',
            name='owner_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='id создателя'),
        ),
    ]
