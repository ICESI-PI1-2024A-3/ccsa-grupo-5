from ..models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import Permission

class UserForm(UserCreationForm):
    roles = forms.ChoiceField(choices=[('admin', 'Admin'),
        ('leader', 'Lider de Proceso'),
        ('manager', 'Gestor de Contratacion')])
    class Meta:
        model = User
        
        fields = ['first_name', 'last_name', 'password1', 'password2', 'email', 'username']