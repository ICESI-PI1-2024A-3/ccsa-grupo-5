"""
View function to delete an observation.
"""

from itertools import chain
from django.http import HttpResponse, JsonResponse
from django.core.serializers import serialize
from django.shortcuts import get_object_or_404, redirect, render
from ..forms import *
from django.db import transaction
from ..models import *
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required
from login.permissions import groupRequired

@login_required
def deleteObservation(request, observationId, petitionId):
    """
    Delete an observation.

    Retrieves the observation by its ID. If a POST request is received,
    deletes the observation and redirects to the viewPetition page.

    Args:
        request: HttpRequest object.
        observationId: ID of the observation to delete.

    Returns:
        If a POST request is received:
            Redirects to the viewPetition page.
    """
    observation = get_object_or_404(Observation, pk=observationId)
    
    if request.method == 'POST':
        if "eliminar" in request.POST:
            observation.delete()
            return redirect("showPetition", petitionId=petitionId)
        elif "cancelar" in request.POST:
            return redirect("showPetition", petitionId=petitionId)
        
    return render(request, "deleteObservation.html")
    
