# Generated by Django 5.0.4 on 2024-05-06 04:36

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('petition', '0010_alter_petition_petitiondate'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=255, verbose_name='Descripción')),
                ('date', models.DateField(auto_now_add=True, verbose_name='Fecha')),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='notificationUser', to=settings.AUTH_USER_MODEL, verbose_name='Remitente')),
                ('petition', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notifications', to='petition.petition', verbose_name='Petición')),
            ],
            options={
                'verbose_name': 'Notificación',
                'verbose_name_plural': 'Notificaciones',
            },
        ),
    ]
