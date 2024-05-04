"""
View function to assign a user to a petition.
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

from django.db.models.signals import post_save
from notify.signals import notify
from notify.utils.models import notify_signals

@login_required
@groupRequired('Admin', 'Lider de Proceso')
def assignUserToPetition(request, petitionId):
    """
    Assign a user to a petition.

    Retrieves the petition by its ID. If a POST request is received,
    checks if the "assign" or "cancel" button is clicked. If "assign"
    button is clicked, assigns the selected user to the petition and
    saves the assignment. If "cancel" button is clicked, redirects
    to the showPetition page. If a GET request is received, renders
    the assignUserToPetition.html template with the petition and
    available users.

    Args:
        request: HttpRequest object.
        petitionId: ID of the petition to assign a user to.

    Returns:
        If a POST request is received:
            If "assign" button is clicked, redirects to the showPetition page.
            If "cancel" button is clicked, redirects to the showPetition page.
        If a GET request is received:
            Rendered assignUserToPetition.html template with the petition and users.
    """
    petition = Petition.objects.get(pk=petitionId)
    
    if request.method == 'POST':
        if 'assign' in request.POST:
            user_id = request.POST['user']
            user = User.objects.get(pk=user_id)
            petition.user = user
            petition.userAsigner = User.objects.get(pk=request.user.id)
            petition.save()
            notify.send(petition, destiny=user, verb="ha sido asignado a la peticion "+petitionId, level="success")
            post_save.connect(notify_signals, sender=petition)
            return redirect('showPetition', petitionId=petitionId)
        elif 'cancel' in request.POST:
            return redirect('showPetition', petitionId=petitionId)
    else:
        users = User.objects.all()
        return render(request, 'assignUserToPetition.html', {'petition': petition, 'users': users})