from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Group
from django.http import HttpResponse
from ..forms import loginForm, userForm
from django.contrib import messages
from django.views.decorators.cache import never_cache
from ..permissions import groupRequired


@groupRequired("Admin")
def signup(request):
    """
    View for signing up new users with different roles.

    Requires 'Admin' group permission.

    GET: Renders signup form.
    POST: Handles form submission to create new user accounts.
    """
    if request.method == "GET":
        form = userForm.UserForm()
        return render(request, "signup.html", {"form": form})
    else:
        form = userForm.UserForm(request.POST)
        if form.is_valid():
            user = form.save()
            roles = form.cleaned_data.get("roles")
            # Display success message
            messages.success(
                request,
                "Usuario creado satisfactoriamente"
            )

            if roles:
                # Assign roles and permissions based on form selection
                if roles == "admin":
                    group = Group.objects.get(name="Admin")
                    user.is_staff = True
                    user.is_superuser = True
                    user.groups.add(group)
                    user.save()
                elif roles == "leader":
                    group = Group.objects.get(name="Lider de Proceso")
                    user.groups.add(group)
                    user.save()
                elif roles == "manager":
                    group = Group.objects.get(name="Gestor de Contratacion")
                    user.groups.add(group)
                    user.save()

            return render(request, "signup.html", {"form": form})
        # Capture form error messages
        else:
            for field, errors in form.errors.items():
                if field == "first_name":
                    field = "Nombre"
                elif field == "last_name":
                    field = "Apellido"
                elif field == "email":
                    field = "Correo electrónico"
                elif field == "username":
                    field = "Cedula"
                elif field == "password1":
                    field = "Contraseña"
                elif field == "password2":
                    field = "Confirmar contraseña"
                for error in errors:
                    messages.error(
                        request,
                        f"Error en {field}: {error}"
                    )
            return render(request, "signup.html", {"form": form})
