from django.shortcuts import render, redirect
from ..models import *

def updateTasks(request, petition_id):
    if request.method == 'POST':
        # Obtener el ID de las tareas seleccionadas del formulario
        selected_task_ids = request.POST.getlist('tasks')

        # Obtener los IDs de las tareas que ya estaban seleccionadas anteriormente
        previously_selected_task_ids = Task.objects.filter(petition_id=petition_id, isComplete=True).values_list('id', flat=True)

        # Obtener los IDs de las tareas que deben cambiar su estado
        tasks_to_toggle = list(set(selected_task_ids) - set(previously_selected_task_ids))

        # Actualizar el estado de las tareas que deben cambiar su estado
        Task.objects.filter(id__in=tasks_to_toggle).update(isComplete=True)

        # Actualizar el estado de las tareas que deben cambiar su estado de completo a incompleto
        Task.objects.exclude(id__in=selected_task_ids).filter(petition_id=petition_id, isComplete=True).update(isComplete=False)

        petition = Petition.objects.get(pk=petition_id)

        if petition.getPercentage() == 100:
            petition.state = "aprobado"
            petition.save()

            
            notification = Notification.objects.create(
            description="Se aprobó la solicitud " + str(petition_id),
            date=timezone.now().date(),
            time=timezone.localtime(),
            author=request.user,  # Asignar el usuario como autor
            petition=petition  # Asignar la petición asociada
            )


    # Redirigir de vuelta a la página de la petición después de actualizar las tareas
    return redirect('showPetition', petitionId=petition_id)
