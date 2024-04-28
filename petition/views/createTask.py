"""
View function to create a new task.
"""

from itertools import chain
from django.http import HttpResponse, JsonResponse
from django.core.serializers import serialize
from django.shortcuts import get_object_or_404, redirect, render
from ..forms import createNewTask
from django.db import transaction
from ..models import *
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required
from login.permissions import groupRequired

@login_required
@groupRequired('Admin')
def createTask(request, petitionId):
    
    if request.method == 'POST':
        form = createNewTask.CreateNewTask(request.POST)
        if form.is_valid():
            form.petitionId = petitionId
            form.save(user=request.user)
            return redirect('viewTask', petitionId)
    else:
        form = createNewTask.CreateNewTask()
    return render(request, 'createTask.html', {'form': form, 'petitionId':petitionId})
