from django.urls import path
from .views import index, createMonitoring, selectTypePetition, createOther, viewPetition, rejectPetition, showPetition, deletePetition, createObservation, deleteObservation, editObservation, assignUserToPetition, viewPetitionWithoutUser
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('index', index.index, name="index"),
    path('createMonitoring', createMonitoring.createMonitoring, name="createMonitoring"),
    path('selectTypePetition', selectTypePetition.selectTypePetition, name="selectTypePetition"),
    path('createOther', createOther.createOther, name="createOther"),
    path('viewPetition', viewPetition.viewPetition, name="viewPetition"),
    path('rejectPetition/<int:petitionId>/', rejectPetition.rejectPetition, name="rejectPetition"),
    path('showPetition/<int:petitionId>/', showPetition.showPetition, name="showPetition"),
    path('deletePetition/<int:petitionId>', deletePetition.deletePetition, name="deletePetition"),
    path('createObservation/<int:petitionId>', createObservation.createObservation , name="createObservation"),
    path('deleteObservation/<int:observationId>', deleteObservation.deleteObservation, name="deleteObservation"),
    path('editObservation/<int:petitionId>/<int:observationId>', editObservation.editObservation, name="editObservation"),
    path('assignUserToPetition/<int:petitionId>', assignUserToPetition.assignUserToPetition, name="assignPetition"),
    path('viewPetitionWithoutUser', viewPetitionWithoutUser.viewPetitionWithoutUser, name="viewPetitionWithoutUser")] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

