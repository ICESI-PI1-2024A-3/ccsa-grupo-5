from django.urls import path
from .views import login, signup, logoutSesion
from django.contrib.auth.forms import UserCreationForm

urlpatterns = [
    #('', views.index, name="index"),
    path('', login.login, name="login"),
    path('signup', signup.signup, name="signup"),
    path('logoutSesion', logoutSesion.logoutSesion, name="logoutSesion")
]
