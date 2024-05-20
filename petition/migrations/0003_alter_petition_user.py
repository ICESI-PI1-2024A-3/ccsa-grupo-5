# Generated by Django 5.0.3 on 2024-03-10 22:02

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('petition', '0002_petition_petitiondate'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='petition',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='petitionUser', to=settings.AUTH_USER_MODEL),
        ),
    ]