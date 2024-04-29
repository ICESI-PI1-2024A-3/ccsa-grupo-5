"""
View function to follow up a petition.
"""

from itertools import chain
from django.http import Http404, HttpResponse, JsonResponse
from django.core.serializers import serialize
from django.shortcuts import get_object_or_404, redirect, render

from login.permissions import groupRequired
from ..forms import *
from django.db import transaction
from ..models import *
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required

@login_required
@groupRequired('Gestor de Contratacion')
def followUpPetition(request, petitionId):
    try:
        petition = Petition.objects.get(pk=petitionId)
        tasks = Task.objects.filter(petition=petition)
        return render(request, 'followUpPetition.html', {'petition': petition, 'tasks': tasks})
    except Petition.DoesNotExist:
        raise Http404('La solicitud no se encuentra')
    