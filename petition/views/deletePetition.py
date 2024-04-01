"""
View function to delete a petition.
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

@login_required
def deletePetition(request, petitionId):
    """
    Delete a petition.

    Retrieves the petition by its ID. If a POST request is received,
    deletes the petition and redirects to the viewPetition page.

    Args:
        request: HttpRequest object.
        petitionId: ID of the petition to delete.

    Returns:
        If a POST request is received:
            Redirects to the viewPetition page.
    """
    petition = get_object_or_404(Petition, pk=petitionId)
    
    if request.method == 'POST':
        petition.delete()
        return redirect('viewPetition')
