from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

class User(AbstractUser):
    cedula = models.CharField(max_length=15, blank=True, null=True, unique=True)
    

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    
    groups = models.ManyToManyField(Group, related_name='groups')
    user_permissions = models.ManyToManyField(Permission, related_name='user_permissions')