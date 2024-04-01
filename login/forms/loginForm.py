from ..models import User
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import Permission

class LoginForm(AuthenticationForm):
    """
    Form for user login.
    """
    class Meta:
        """
        Metadata class specifying the model for the form.
        """
        model = User
