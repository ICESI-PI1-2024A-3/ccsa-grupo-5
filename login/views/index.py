from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import logout
from django.views.decorators.cache import never_cache
from django.contrib.auth.models import User, Group

@login_required
def index(request):
    """
    View for the index page.

    This view renders the index page when the user is authenticated.
    """
    return render(request, "index.html")
