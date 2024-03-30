from django.contrib.auth.models import Group
from django.db.models.signals import post_migrate
from django.dispatch import receiver
from django.contrib.auth.decorators import user_passes_test





def create_groups():
        Group.objects.get_or_create(name='Admin')
        Group.objects.get_or_create(name='Lider de Proceso')
        Group.objects.get_or_create(name='Gestor de Contratacion')
        
def groupRequired(*groupNames):
    """
    Decorator for views that checks whether a user is in the required group(s).
    """
    def inGroup(user):
        return user.groups.filter(name__in=groupNames).exists()

    return user_passes_test(inGroup)