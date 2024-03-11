from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('createMonitoring', views.createMonitoring, name="createMonitoring"),
    path('selectTypePetition', views.selectTypePetition, name="selectTypePetition"),
    path('createOther', views.createOther, name="createOther"),
    path('petitions', views.petitions, name="petitions"),
    path('editPetition/<int:solicitudId>/', views.editPetition, name="editPetition")
]