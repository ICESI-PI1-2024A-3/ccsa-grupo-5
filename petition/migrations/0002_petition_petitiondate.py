# Generated by Django 5.0.2 on 2024-03-10 05:48

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('petition', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='petition',
            name='petitionDate',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
