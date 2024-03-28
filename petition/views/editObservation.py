from itertools import chain
from django.http import HttpResponse, JsonResponse
from django.core.serializers import serialize
from django.shortcuts import get_object_or_404, redirect, render
from ..forms import createNewObservation
from django.db import transaction
from ..models import *
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required



@login_required
def editObservation(request, petitionId, observationId):
    # Obtener la observación a editar
    observation = get_object_or_404(Observation, pk=observationId)
    
    if request.method == 'POST':
        # Si el formulario se envió con datos, procesar los datos del formulario
        form = createNewObservation.CreateNewObservation(request.POST, instance=observation)
        if form.is_valid():
            # Obtener la instancia de la observación pero no guardarla todavía
            observation = form.save(user=request.user,commit=False)
            
            # Asignar la ID de la petición a la observación
            observation.petition_id = petitionId
            
            # Guardar la observación actualizada en la base de datos
            observation.save()
    
            # Redirigir a la página de detalles de la solicitud
            return redirect('showPetition', petitionId=petitionId)
    else:
        # Si es un método GET, renderizar el formulario de edición con los datos de la observación actual
        form = createNewObservation.CreateNewObservation(instance=observation)
    
    # Renderizar el formulario de edición
    return render(request, 'editObservation.html', {'form': form})