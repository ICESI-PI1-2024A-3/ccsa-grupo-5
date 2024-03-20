from .models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['name', 'lastName', 'password1', 'password2', 'email']
    
class LoginForm(AuthenticationForm):
    
    identification = forms.CharField(max_length=15)  
    password = forms.CharField(widget=forms.PasswordInput)
    
    #class Meta:
    #    model = User
