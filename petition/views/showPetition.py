"""
View function to display a specific petition.
"""

from itertools import chain
from django.http import Http404, HttpResponse, JsonResponse
from django.core.serializers import serialize
from django.shortcuts import get_object_or_404, redirect, render
from ..forms import *
from django.db import transaction
from ..models import *
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required

@login_required
def showPetition(request, petitionId):
    """
    Render a page displaying a specific petition.

    Attempts to retrieve the petition as an Other object. If successful,
    retrieves related observations and renders a template for Other petitions.
    If not found as an Other, attempts to retrieve the petition as a Monitoring
    object. If successful, retrieves related observations and renders a template
    for Monitoring petitions. If the petition is not found, raises a 404 error.

    Args:
        request: HttpRequest object.
        petitionId: ID of the petition to display.

    Returns:
        Rendered viewPetitionO.html template for Other petitions or viewPetitionM.html
        template for Monitoring petitions with 'solicitud', 'observations', and 'petitionId'
        context.
    Raises:
        Http404: If the petition is not found.
    """
    solicitud = None
    
    # Attempt to get the petition as Other
    try:
        solicitud = Other.objects.get(pk=petitionId)
        observations = Observation.objects.filter(petition=solicitud)
        tasks = Task.objects.filter(petition=solicitud)
        return render(request, 'viewPetitionO.html', {'solicitud': solicitud, 'tasks':tasks,'observations': observations, 'petitionId': petitionId})
    except Other.DoesNotExist:
        pass
    
    # If not found as Other, attempt to get it as Monitoring
    try:
        solicitud = Monitoring.objects.get(pk=petitionId)
        observations = Observation.objects.filter(petition=solicitud)
        tasks = Task.objects.filter(petition=solicitud)
        return render(request, 'viewPetitionM.html', {'solicitud': solicitud, 'tasks':tasks,'observations': observations, 'petitionId': petitionId})
    except Monitoring.DoesNotExist:
        pass
    
    # If petition not found, raise 404 error
    raise Http404('La solicitud no se encuentra')