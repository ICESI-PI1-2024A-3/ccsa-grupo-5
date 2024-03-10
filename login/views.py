from django.contrib.auth.forms import AuthenticationForm 
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth.models import User
from django.http import HttpResponse
import login
from .forms import UserForm


# Create your views here.
def index(request):
    return render(request, 'index.html')

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return HttpResponse("Inicio de sesión exitoso")
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def signup(request):
    if request.method == "GET":
        form = UserForm()
        return render(request, 'signup.html', {'form': form})
    else:
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Usuario creado satisfactoriamente")
        else:
            return render(request, 'signup.html', {'form': form})
        

        



