"""
View function to display the tasks.
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
def viewTask(request,petitionId):
    petition = None
    
    try:
        petition = Petition.objects.get(pk=petitionId)
        tasks = Task.objects.filter(petition=petition)
        return render(request, 'viewTask.html', {'tasks': tasks, 'petitionId':petitionId})
    except Task.DoesNotExist:
        pass
    
    raise Http404('No fueron encontradas las tareas')