from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

class User(AbstractUser):
    # Eliminar el campo 'username' si no se desea utilizar
    username = models.CharField(max_length=15, unique=True)
    
    

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    
    