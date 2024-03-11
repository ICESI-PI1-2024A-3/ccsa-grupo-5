from .models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'password1', 'password2', 'email', 'username' ]
    
class LoginForm(AuthenticationForm):
    class Meta:
        model = User
