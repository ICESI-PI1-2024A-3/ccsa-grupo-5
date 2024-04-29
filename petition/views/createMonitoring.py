"""
View function to create a new monitoring petition.
"""

from itertools import chain
from django.http import HttpResponse, JsonResponse
from django.core.serializers import serialize
from django.shortcuts import get_object_or_404, redirect, render
from ..forms import createNewMonitoringPetition
from django.db import transaction
from ..models import *
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required
from login.permissions import groupRequired

@login_required
@groupRequired('Admin', 'Lider de Proceso')
@transaction.atomic
def createMonitoring(request):
    """
    Create a new monitoring petition.

    Renders the 'createMonitoring.html' template with a form to create
    a new monitoring petition. If a POST request is received with valid
    form data, saves the form and redirects to the viewPetition page.

    Args:
        request: HttpRequest object.

    Returns:
        If a POST request is received with valid form data:
            Redirects to the viewPetition page.
        If a GET request is received or form data is invalid:
            Rendered createMonitoring.html template with the form.
    """
    if request.method == 'POST':
        form = createNewMonitoringPetition.CreateNewMonitoringPetition(request.POST, request.FILES)
        if form.is_valid():
            tes = form.save(request.user)
            
            petitionId = tes.id
            
            taskPredeterminate = TaskPredeterminate.objects.all()
            
            petition = Petition.objects.get(pk=petitionId)
            
            for task in taskPredeterminate:
                Task.objects.create(description=task.description, petition=petition)
                
            return redirect('viewTask', petitionId)
    else:
        form = createNewMonitoringPetition.CreateNewMonitoringPetition()
    return render(request, 'createMonitoring.html', {'form': form})
