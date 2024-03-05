from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    UserTypeChoices = [
        ('admin', 'Admin'),
        ('processLeader', 'Líder de Procesos'),
        ('processManager', 'Gestor de Procesos'),
    ]

    userType = models.CharField(max_length=20, choices=UserTypeChoices, default='processManager')
    
    groups = models.ManyToManyField('auth.Group', related_name='auth_users')
    user_permissions = models.ManyToManyField('auth.Permission', related_name='auth_users')

    def __str__(self):
        return f'{self.username} ({self.userType})'
