from django.urls import path
from . import views

urlpatterns = [
    #('', views.index, name="index"),
    path('', views.login, name="login")
    
]