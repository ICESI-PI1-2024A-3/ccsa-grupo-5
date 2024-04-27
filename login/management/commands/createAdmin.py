from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError

class Command(BaseCommand):
    """
    Management command to create a superuser and add them to the Admin group.
    """

    help = 'Crea un superusuario y agrégalo al grupo Admin'

    def handle(self, *args, **options):
        """
        Handle command execution.
        """
        User = get_user_model()
        username = input('Ingresa el identificador: ')
        first_name = input('Ingresa el nombre: ')
        last_name = input('Ingresa el apellido: ')
        email = input('Ingresa el correo electrónico: ')
        
        while True:
            password1 = input('Ingresa la contraseña: ')
            password2 = input('Confirma la contraseña: ')

            if password1 == password2:
                break
            else:
                self.stdout.write(self.style.ERROR('Las contraseñas no coinciden. Por favor, inténtalo de nuevo.'))

        try:
            # Create the superuser
            superuser = User.objects.create_superuser(username=username, first_name = first_name, last_name = last_name , email=email, password=password1)
        except ValidationError as e:
            self.stderr.write(self.style.ERROR(f'Error creando superusuario: {", ".join(e)}'))
            return

        # Add the superuser to the Admin group
        group_name = "Admin"
        group, created = Group.objects.get_or_create(name=group_name)
        superuser.groups.add(group)
        superuser.save()

        self.stdout.write(self.style.SUCCESS('Superusuario creado exitosamente y agregado al grupo Admin'))
