"""
View function to handle rejecting a petition.
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
def rejectPetition(request, petitionId):
    """
    Handle rejecting a petition.

    Retrieves the petition by its ID. If the petition is found,
    processes the rejection if a POST request is received.

    Args:
        request: HttpRequest object.
        petitionId: ID of the petition to reject.

    Returns:
        If a POST request is received:
            If "rechazar" button is clicked, updates petition state to "rechazado"
            and redirects to the showPetition page.
            If "cancelar" button is clicked, redirects to the showPetition page.
        If a GET request is received:
            Rendered rejectPetition.html template.
    
    Raises:
        Http404: If the petition is not found.
    """
    try:
        petition = Petition.objects.get(pk=petitionId)
    except Petition.DoesNotExist:
        raise Http404("La solicitud no se encuentra")

    if request.method == "POST":
        if "rechazar" in request.POST:
            # Update petition state to "rechazado" if "rechazar" button is clicked
            petition.state = "rechazado"
            petition.save()
            return redirect("showPetition", petitionId=petitionId)
        elif "cancelar" in request.POST:
            # Redirect to showPetition page if "cancelar" button is clicked
            return redirect("showPetition", petitionId=petitionId)

    # Render rejectPetition.html template for GET requests
    return render(request, "rejectPetition.html")