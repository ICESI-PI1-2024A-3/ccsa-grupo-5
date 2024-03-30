from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
import login
from login.permissions import createGroups
from ..forms import loginForm, userForm
from django.contrib import messages
from django.contrib.auth import logout
from django.views.decorators.cache import never_cache
from django.contrib.auth.models import User, Group
from ..permissions import groupRequired

@groupRequired('Admin')
def signup(request):
    createGroups()
    if request.method == "GET":
        form = userForm.UserForm()
        return render(request, "signup.html", {"form": form})
    else:
        form = userForm.UserForm(request.POST)
        if form.is_valid():
            user = form.save()
            roles = form.cleaned_data.get("roles")
            # Mostrar alerta de éxito
            messages.success(request, "Usuario creado satisfactoriamente")

            if roles:
                # Asignar roles y permisos según la selección del formulario
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
        # Capturar mensajes de error del formulario
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
                    messages.error(request, f"Error en {field}: {error}")
            return render(request, "signup.html", {"form": form})
