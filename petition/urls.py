from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name="index"),
    path('createMonitoring', views.createMonitoring, name="createMonitoring"),
    path('selectTypePetition', views.selectTypePetition, name="selectTypePetition"),
    path('createOther', views.createOther, name="createOther"),
    path('petitions', views.petitions, name="petitions"),
    path('editPetition/<int:solicitudId>/', views.editPetition, name="editPetition")
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)