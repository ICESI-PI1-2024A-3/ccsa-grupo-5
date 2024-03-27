from itertools import chain
from django.http import HttpResponse, JsonResponse
from django.core.serializers import serialize
from django.shortcuts import get_object_or_404, redirect, render
from ..forms import *
from django.db import transaction
from ..models import *
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required




    
@login_required
def showPetition(request, petitionId):
    solicitud = None
    
    # Intenta obtener la solicitud como Other
    try:
        solicitud = Other.objects.get(pk=petitionId)
        observations = Observation.objects.filter(petition=solicitud)
        return render(request, 'viewPetitionO.html', {'solicitud': solicitud, 'observations': observations, 'petitionId': petitionId})
    except Other.DoesNotExist:
        pass
    
    # Si no es una solicitud de Other, intenta obtenerla como Monitoring
    try:
        solicitud = Monitoring.objects.get(pk=petitionId)
        observations = Observation.objects.filter(petition=solicitud)
        return render(request, 'viewPetitionM.html', {'solicitud': solicitud, 'observations': observations, 'petitionId': petitionId})
    except Monitoring.DoesNotExist:
        pass
    
    # Si no se encuentra la solicitud, renderiza una plantilla de error o maneja el caso según sea necesario
    return render(request, 'error.html', {'mensaje': 'La solicitud no se encuentra'})