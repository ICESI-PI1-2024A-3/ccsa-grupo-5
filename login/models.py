from django.db import models
from django.contrib.auth.models import AbstractUser, Group, PermissionsMixin
from django.db.models.signals import post_migrate
from django.dispatch import receiver


class User(AbstractUser, PermissionsMixin):
    # Eliminar el campo 'username' si no se desea utilizar
    username = models.CharField(max_length=15, unique=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def getGroup(self):
        return ", ".join([group.name for group in self.groups.all()])

    getGroup.short_description = "Rol"
