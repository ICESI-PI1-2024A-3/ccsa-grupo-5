from ..models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import Permission

class LoginForm(AuthenticationForm):
    class Meta:
        model = User
