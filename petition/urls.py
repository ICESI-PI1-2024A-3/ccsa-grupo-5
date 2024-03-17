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
    path('rejectPetition/<int:petitionId>/', views.rejectPetition, name="rejectPetition"),
    path('showPetition/<int:petitionId>/', views.showPetition, name="showPetition"),
    path('deletePetition/<int:petitionId>', views.deletePetition, name="deletePetition"),
    path('assignUserToPetition/<int:petitionId>', views.assignUserToPetition, name="assignPetition")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

