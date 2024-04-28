from django.urls import path
from .views import login, signup, logoutSesion
from django.contrib.auth.forms import UserCreationForm

urlpatterns = [
    #('', views.index, name="index"),
    path('', login.login, name="login"),
    path('usuario/crear', signup.signup, name="signup"),
    path('cerrarSesion', logoutSesion.logoutSesion, name="logoutSesion")
]
