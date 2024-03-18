from django.urls import path
from . import views
from django.contrib.auth.forms import UserCreationForm

urlpatterns = [
    #('', views.index, name="index"),
    path('', views.login, name="login"),
    path('signup', views.signup, name="signup"),
    path('logoutSesion', views.logoutSesion, name="logoutSesion")
]
