from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse
from .forms import UserForm


# Create your views here.
def index(request):
    return render(request, 'index.html')

def login(request):
    return render(request, 'login.html')

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
        

        



