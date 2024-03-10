from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('createMonitoring', views.createMoniroring, name="createMonitoring"),
    path('selectTypePetition', views.selectTypePetition, name="selectTypePetition"),
    path('createOtro', views.otro, name="createOtro")
]