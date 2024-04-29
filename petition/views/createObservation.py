"""
View function to create a new observation.
"""

from itertools import chain
from django.http import HttpResponse, JsonResponse
from django.core.serializers import serialize
from django.shortcuts import get_object_or_404, redirect, render
from ..forms import createNewObservation
from django.db import transaction
from ..models import *
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required
from login.permissions import groupRequired

@login_required
def createObservation(request, petitionId):
    """
    Create a new observation.

    Renders the 'createObservation.html' template with a form to create
    a new observation for the specified petition. If a POST request is received
    with valid form data, saves the form and redirects to the showPetition page
    for the specified petition.

    Args:
        request: HttpRequest object.
        petitionId: ID of the petition to create the observation for.

    Returns:
        If a POST request is received with valid form data:
            Redirects to the showPetition page for the specified petition.
        If a GET request is received or form data is invalid:
            Rendered createObservation.html template with the form and petitionId.
    """
    if request.method == 'POST':
        form = createNewObservation.CreateNewObservation(request.POST)
        if form.is_valid():
            form.petitionId = petitionId 
            form.save(user=request.user)
            return redirect('showPetition', petitionId=petitionId)
    else:
        form = createNewObservation.CreateNewObservation()
    return render(request, 'createObservation.html', {'form': form, 'petitionId': petitionId})
