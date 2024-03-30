from django.contrib.auth.models import Group
from django.db.models.signals import post_migrate
from django.dispatch import receiver
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from .models import User
from petition.models import Petition, Observation


@receiver(post_migrate)
def assignPermissions(sender, **kwargs):
    # Obtener ContentType para los modelos relevantes
    userContentType = ContentType.objects.get_for_model(User)
    petitionContentType = ContentType.objects.get_for_model(Petition)
    observationContentType = ContentType.objects.get_for_model(Observation)

    # Obtener o crear los grupos
    gestorGroup, _ = Group.objects.get_or_create(name="Gestor de Contratacion")
    liderGroup, _ = Group.objects.get_or_create(name="Lider de Proceso")
    admin, _ = Group.objects.get_or_create(name="Admin")

    # Asignar todos los permisos predeterminados a Gestor de Contratacion
    admin.permissions.set(Permission.objects.all())

    # Crear y asignar permisos a Lider de Proceso
    liderGroup.permissions.add(
        Permission.objects.get(
            content_type=observationContentType, codename="add_observation"
        ),
        Permission.objects.get(
            content_type=observationContentType, codename="change_observation"
        ),
        Permission.objects.get(
            content_type=observationContentType, codename="delete_observation"
        ),
        Permission.objects.get(
            content_type=observationContentType, codename="view_observation"
        ),
        Permission.objects.get(
            content_type=petitionContentType, codename="add_petition"
        ),
        Permission.objects.get(
            content_type=petitionContentType, codename="change_petition"
        ),
        Permission.objects.get(
            content_type=petitionContentType, codename="delete_petition"
        ),
        Permission.objects.get(
            content_type=petitionContentType, codename="view_petition"
        ),
        Permission.objects.get(content_type=userContentType, codename="view_user"),
    )

    # Crear y asignar permisos a Gestor de Contratacion
    liderGroup.permissions.add(
        Permission.objects.get(
            content_type=observationContentType, codename="add_observation"
        ),
        Permission.objects.get(
            content_type=observationContentType, codename="change_observation"
        ),
        Permission.objects.get(
            content_type=observationContentType, codename="delete_observation"
        ),
        Permission.objects.get(
            content_type=observationContentType, codename="view_observation"
        ),
        Permission.objects.get(
            content_type=petitionContentType, codename="change_petition"
        ),
        Permission.objects.get(
            content_type=petitionContentType, codename="view_petition"
        ),
        Permission.objects.get(content_type=userContentType, codename="view_user"),
    )
