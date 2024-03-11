from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name="index"),
    path('createMonitoring', views.createMonitoring, name="createMonitoring"),
    path('selectTypePetition', views.selectTypePetition, name="selectTypePetition"),
    path('createOther', views.createOther, name="createOther"),
    path('viewPetition', views.viewPetition, name="viewPetition"),
    path('editPetition/<int:petitionId>/', views.editPetition, name="editPetition"),
    path('deletePetition/<int:petitionId>', views.deletePetition, name="deletePetition")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

