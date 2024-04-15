from ..models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import Permission

class UserForm(UserCreationForm):
    """
    Form for user creation with additional fields.
    """
    roles = forms.ChoiceField(
        choices=[
            ("leader", "Líder de Proceso"),
            ("manager", "Gestor de Contratación"),
        ]
    )

    class Meta:
        """
        Metadata class specifying the model and fields for the form.
        """
        model = User
        fields = [
            "first_name",
            "last_name",
            "password1",
            "password2",
            "email",
            "username",
        ]
