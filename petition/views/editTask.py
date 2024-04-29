"""
View function to edit an task predeterminate.
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

@login_required
def editTask(request, petitionId, taskId):
    
    # Get the observation to edit
    task = get_object_or_404(Task, pk=taskId)
    
    if request.method == 'POST':
        # If the form is submitted with data, process the form data
        form = createNewTask.CreateNewTask(request.POST, instance=task)
        if form.is_valid():
            
            task = form.save(user=request.user, commit=False)
            
            task.petition_id = petitionId
            
            # Save the updated task to the database
            task.save()
    
            # Redirect to the viewTask page
            return redirect('viewTask', petitionId)
    else:
        # If it's a GET method, render the edit form with the current task data
        form = createNewTask.CreateNewTask(instance=task)
    
    # Render the edit form
    return render(request, 'editTask.html', {'form': form})
