from django.contrib.auth.forms import AuthenticationForm 
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
import login
from .forms import LoginForm, UserForm
from django.contrib import messages
from django.contrib.auth import logout
from django.views.decorators.cache import never_cache



# Create your views here.
@login_required
def index(request):
    return render(request, 'index.html')

@never_cache
def login(request):
        
    if request.method == 'POST':
        form = LoginForm(request, data = request.POST )
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('index') 
        else:
            messages.error(request, 'Acceso inválido. Por favor, inténtelo otra vez.')
    else:
        form = LoginForm()
        
    isAuthenticated = request.user.is_authenticated
    return render(request, 'login.html', {'form': form, 'is_authenticated': isAuthenticated})


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
        
@login_required        
def logoutSesion(request):
    logout(request)
    return redirect('login')  

        

        



