# Generated by Django 5.0.4 on 2024-05-06 05:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('petition', '0011_notification'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='time',
            field=models.TimeField(default=datetime.datetime(2024, 5, 6, 5, 14, 43, 710672, tzinfo=datetime.timezone.utc), null=True, verbose_name='Hora'),
        ),
        migrations.AlterField(
            model_name='notification',
            name='date',
            field=models.DateField(default=datetime.date(2024, 5, 6), null=True, verbose_name='Fecha'),
        ),
    ]
