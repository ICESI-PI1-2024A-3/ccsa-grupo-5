from django.db import models
from django.contrib.auth.models import AbstractUser, Group, PermissionsMixin
from django.db.models.signals import post_migrate
from django.dispatch import receiver


class User(AbstractUser, PermissionsMixin):
    """
    Custom user model with additional fields.

    Inherits from:
        AbstractUser: Django's built-in abstract user model.
        PermissionsMixin: Provides the methods necessary to support Django's permission framework.

    Attributes:
        username (str): The unique identifier for the user. Max length is 15 characters.
    """
    username = models.CharField(
        max_length=15, unique=True, verbose_name="identificador"
    )

    def __str__(self):
        """
        String representation of the user.

        Returns:
            str: The first name and last name of the user.
        """
        return f"{self.first_name} {self.last_name}"

    def getGroup(self):
        """
        Method to retrieve user's group(s).

        Returns:
            str: A comma-separated string of the user's group names.
        """
        return ", ".join([group.name for group in self.groups.all()])

    getGroup.short_description = "Rol"
