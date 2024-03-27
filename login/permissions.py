from django.contrib.auth.models import Group
from django.db.models.signals import post_migrate
from django.dispatch import receiver




def create_groups():
        Group.objects.get_or_create(name='Admin')
        Group.objects.get_or_create(name='Lider de Proceso')
        Group.objects.get_or_create(name='Gestor de Contratacion')