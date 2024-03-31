from django.contrib.auth.models import Group
from django.db.models.signals import post_migrate
from django.dispatch import receiver
from django.contrib.auth.decorators import user_passes_test


def groupRequired(*groupNames):
    """
    Decorator for views that checks whether a user is in the required group(s).
    """

    def inGroup(user):
        return user.groups.filter(name__in=groupNames).exists()

    return user_passes_test(inGroup)


from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from .models import User
from petition.models import Petition, Observation


def groupRequired(*groupNames):
    """
    Decorator for views that checks whether a user is in the required group(s).
    """

    def inGroup(user):
        return user.groups.filter(name__in=groupNames).exists()

    return user_passes_test(inGroup)


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
        Permission.objects.get_or_create(
            content_type=observationContentType,
            codename="add_observation",
            defaults={"name": "Can add observation"},
        )[0],
        Permission.objects.get_or_create(
            content_type=observationContentType,
            codename="change_observation",
            defaults={"name": "Can change observation"},
        )[0],
        Permission.objects.get_or_create(
            content_type=observationContentType,
            codename="delete_observation",
            defaults={"name": "Can delete observation"},
        )[0],
        Permission.objects.get_or_create(
            content_type=observationContentType,
            codename="view_observation",
            defaults={"name": "Can view observation"},
        )[0],
        Permission.objects.get_or_create(
            content_type=petitionContentType,
            codename="add_petition",
            defaults={"name": "Can add petition"},
        )[0],
        Permission.objects.get_or_create(
            content_type=petitionContentType,
            codename="change_petition",
            defaults={"name": "Can change petition"},
        )[0],
        Permission.objects.get_or_create(
            content_type=petitionContentType,
            codename="delete_petition",
            defaults={"name": "Can delete petition"},
        )[0],
        Permission.objects.get_or_create(
            content_type=petitionContentType,
            codename="view_petition",
            defaults={"name": "Can view petition"},
        )[0],
        Permission.objects.get_or_create(
            content_type=userContentType,
            codename="view_user",
            defaults={"name": "Can view user"},
        )[0],
    )

    # Crear y asignar permisos a Gestor de Contratacion
    gestorGroup.permissions.add(
        Permission.objects.get_or_create(
            content_type=observationContentType,
            codename="add_observation",
            defaults={"name": "Can add observation"},
        )[0],
        Permission.objects.get_or_create(
            content_type=observationContentType,
            codename="change_observation",
            defaults={"name": "Can change observation"},
        )[0],
        Permission.objects.get_or_create(
            content_type=observationContentType,
            codename="delete_observation",
            defaults={"name": "Can delete observation"},
        )[0],
        Permission.objects.get_or_create(
            content_type=observationContentType,
            codename="view_observation",
            defaults={"name": "Can view observation"},
        )[0],
        Permission.objects.get_or_create(
            content_type=petitionContentType,
            codename="change_petition",
            defaults={"name": "Can change petition"},
        )[0],
        Permission.objects.get_or_create(
            content_type=petitionContentType,
            codename="view_petition",
            defaults={"name": "Can view petition"},
        )[0],
        Permission.objects.get_or_create(
            content_type=userContentType,
            codename="view_user",
            defaults={"name": "Can view user"},
        )[0],
    )
