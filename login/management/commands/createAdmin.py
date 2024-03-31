from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError

class Command(BaseCommand):
    help = 'Create a superuser and add them to the Admin group'

    def handle(self, *args, **options):
        User = get_user_model()
        username = input('Enter username: ')
        email = input('Enter email: ')
        
        while True:
            password1 = input('Enter password: ')
            password2 = input('Confirm password: ')

            if password1 == password2:
                break
            else:
                self.stdout.write(self.style.ERROR('Passwords do not match. Please try again.'))

        try:
            # Create the superuser
            superuser = User.objects.create_superuser(username=username, email=email, password=password1)
        except ValidationError as e:
            self.stderr.write(self.style.ERROR(f'Error creating superuser: {", ".join(e)}'))
            return

        # Add the superuser to the Admin group
        group_name = "Admin"
        group, created = Group.objects.get_or_create(name=group_name)
        superuser.groups.add(group)
        superuser.save()

        self.stdout.write(self.style.SUCCESS('Superuser created successfully and added to Admin group'))
