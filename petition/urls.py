from django.urls import path

from login.views.error404 import error404
from .views import (
    index,
    createMonitoring,
    selectTypePetition,
    createOther,
    viewPetition,
    rejectPetition,
    showPetition,
    deletePetition,
    createObservation,
    deleteObservation,
    editObservation,
    assignUserToPetition,
    viewPetitionWithoutUser,
    viewTaskPrederminate,
    deleteTaskPredeterminate,
    createTaskPredeterminate,
    editTaskPredeterminate,
    viewTask,
    deleteTask,
    createTask,
    editTask,
    updateTasks,
)
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("index", index.index, name="index"),
    path(
        "solicitud/crearM", createMonitoring.createMonitoring, name="createMonitoring"
    ),
    path(
        "solicitud/seleccionarTipo",
        selectTypePetition.selectTypePetition,
        name="selectTypePetition",
    ),
    path("solicitud/crearO", createOther.createOther, name="createOther"),
    path("solicitud/tabla", viewPetition.viewPetition, name="viewPetition"),
    path(
        "solicitud/rechazar/<int:petitionId>/",
        rejectPetition.rejectPetition,
        name="rejectPetition",
    ),
    path(
        "solicitud/detalles/<int:petitionId>/",
        showPetition.showPetition,
        name="showPetition",
    ),
    path(
        "solicitud/eliminar/<int:petitionId>",
        deletePetition.deletePetition,
        name="deletePetition",
    ),
    path(
        "solicitud/observacion/crear/<int:petitionId>",
        createObservation.createObservation,
        name="createObservation",
    ),
    path(
        "solicitud/observacion/eliminar/<int:observationId>",
        deleteObservation.deleteObservation,
        name="deleteObservation",
    ),
    path(
        "solicitud/observacion/editar/<int:petitionId>/<int:observationId>",
        editObservation.editObservation,
        name="editObservation",
    ),
    path(
        "solicitud/asignarUsuario/<int:petitionId>",
        assignUserToPetition.assignUserToPetition,
        name="assignPetition",
    ),
    path(
        "solicitud/tareasPredeterminadas",
        viewTaskPrederminate.viewTaskPredeterminate,
        name="viewTaskPredeterminate",
    ),
    path(
        "solicitud/tareasPredeterminadas/crear",
        createTaskPredeterminate.createTaskPredeterminate,
        name="createTaskPredeterminate",
    ),
    path(
        "solicitud/tareasPredeterminadas/editar/<int:taskId>",
        editTaskPredeterminate.editTaskPredeterminate,
        name="editTaskPredeterminate",
    ),
    path(
        "solicitud/tareasPredeterminadas/eliminar/<int:taskId>",
        deleteTaskPredeterminate.deleteTaskPredeterminate,
        name="deleteTaskPredeterminate",
    ),
    path("solicitud/tareas/<int:petitionId>", viewTask.viewTask, name="viewTask"),
    path(
        "solicitud/tareas/crear/<int:petitionId>",
        createTask.createTask,
        name="createTask",
    ),
    path(
        "solicitud/tareas/editar/<int:petitionId>/<int:taskId>",
        editTask.editTask,
        name="editTask",
    ),
    path(
        "solicitud/tareas/eliminar/<int:taskId>",
        deleteTask.deleteTask,
        name="deleteTask",
    ),
    path(
        "solicitud/tareas/actualizar/<int:petition_id>/",
        updateTasks.updateTasks,
        name="update_tasks",
    ),
    path(
        "solicitud/tabla/sinAsignar",
        viewPetitionWithoutUser.viewPetitionWithoutUser,
        name="viewPetitionWithoutUser",
    ),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = error404
