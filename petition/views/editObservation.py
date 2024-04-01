"""
View function to edit an observation.
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

@login_required
def editObservation(request, petitionId, observationId):
    """
    Edit an observation.

    Retrieves the observation to edit. If a POST request is received,
    processes the form data. If the form is valid, updates the observation
    in the database and redirects to the showPetition page. If the form
    is not valid or it's a GET request, renders the editObservation.html
    template with the form.

    Args:
        request: HttpRequest object.
        petitionId: ID of the petition associated with the observation.
        observationId: ID of the observation to edit.

    Returns:
        If a POST request is received and the form is valid:
            Redirects to the showPetition page.
        If a GET request is received or the form is not valid:
            Rendered editObservation.html template with the form.
    """
    # Get the observation to edit
    observation = get_object_or_404(Observation, pk=observationId)
    
    if request.method == 'POST':
        # If the form is submitted with data, process the form data
        form = createNewObservation.CreateNewObservation(request.POST, instance=observation)
        if form.is_valid():
            # Get the observation instance but don't save it yet
            observation = form.save(user=request.user, commit=False)
            
            # Assign the petition ID to the observation
            observation.petition_id = petitionId
            
            # Save the updated observation to the database
            observation.save()
    
            # Redirect to the showPetition page
            return redirect('showPetition', petitionId=petitionId)
    else:
        # If it's a GET method, render the edit form with the current observation data
        form = createNewObservation.CreateNewObservation(instance=observation)
    
    # Render the edit form
    return render(request, 'editObservation.html', {'form': form})
