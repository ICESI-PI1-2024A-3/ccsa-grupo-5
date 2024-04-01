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
@groupRequired('Admin', 'Lider de Proceso')
def deleteObservation(request, observationId):
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
        observation.delete()
        return redirect('viewPetition')
