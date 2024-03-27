from django.contrib.auth.forms import AuthenticationForm 
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
import login
from login.permissions import create_groups
from ..forms import LoginForm, UserForm
from django.contrib import messages
from django.contrib.auth import logout
from django.views.decorators.cache import never_cache
from django.contrib.auth.models import User, Group



# Create your views here.
@login_required
def index(request):
    return render(request, 'index.html')