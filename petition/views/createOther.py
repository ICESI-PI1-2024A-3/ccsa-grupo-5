"""
View function to create a new other petition.
"""

from itertools import chain
from django.http import HttpResponse, JsonResponse
from django.core.serializers import serialize
from django.shortcuts import get_object_or_404, redirect, render
from ..forms import createNewOtherPetition
from django.db import transaction
from ..models import *
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required
from login.permissions import groupRequired
from notify import models as nm

from django.db.models.signals import post_save
from notify.signals import notify
from notify.utils.models import notify_signals


@login_required
@groupRequired('Admin', 'Lider de Proceso')
def createOther(request):
    """
    Create a new other petition.

    Renders the 'createOther.html' template with a form to create a new
    other petition. If a POST request is received with valid form data,
    saves the form and redirects to the viewPetition page.

    Args:
        request: HttpRequest object.

    Returns:
        If a POST request is received with valid form data:
            Redirects to the viewPetition page.
        If a GET request is received or form data is invalid:
            Rendered createOther.html template with the form.
    """
    if request.method == 'POST':
        form = createNewOtherPetition.CreateNewOtherPetition(request.POST, request.FILES)
        if form.is_valid():
            tes = form.save(request.user)
            
            petitionId = tes.id
            
            taskPredeterminate = TaskPredeterminate.objects.all()
            
            petition = Petition.objects.get(pk=petitionId)
            
            if tes is None:
                notify.send(actor=petition.userAsigner, destiny=petition.user, verb="Usted ha sido asignado a la peticion "+str(petitionId), level="success", sender=petition.userAsigner)
                post_save.connect(notify_signals, sender=petition.userAsigner)
            
            for task in taskPredeterminate:
                Task.objects.create(description=task.description, petition=petition)
                
            return redirect('viewTask', petitionId)
    else:
        form = createNewOtherPetition.CreateNewOtherPetition()
    return render(request, 'createOther.html', {'form': form})