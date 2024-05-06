from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from ..forms import loginForm, userForm
from django.contrib import messages
from django.contrib.auth import logout
from django.views.decorators.cache import never_cache
from django.contrib.auth.models import User, Group


@never_cache
def login(request):
    """
    View for handling user login.

    This view manages user login functionality. It supports both GET and POST requests.
    For a POST request, it attempts to authenticate the user with the provided credentials.
    If authentication is successful, the user is logged in and redirected to the index page.
    If authentication fails, an error message is displayed.
    """
    if request.method == "POST":
        form = loginForm.LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect("index")
        else:
            messages.error(
                request,
                "Acceso inválido. Por favor, inténtelo otra vez.",
                extra_tags="login_error",
            )
    else:
        form = loginForm.LoginForm()

    isAuthenticated = request.user.is_authenticated
    return render(
        request, "login.html", {"form": form, "is_authenticated": isAuthenticated}
    )
