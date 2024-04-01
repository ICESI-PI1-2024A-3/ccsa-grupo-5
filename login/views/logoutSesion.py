from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Group
from django.http import HttpResponse
from ..forms import loginForm, userForm
from django.contrib import messages
from django.views.decorators.cache import never_cache

@login_required
def logoutSesion(request):
    """
    View for logging out the current user.

    Redirects to the login page after logging out.
    """
    logout(request)
    return redirect("login")
