"""
View function to edit an task predeterminate.
"""

from itertools import chain
from django.http import HttpResponse, JsonResponse
from django.core.serializers import serialize
from django.shortcuts import get_object_or_404, redirect, render
from ..forms import createNewTaskPredeterminate
from django.db import transaction
from ..models import *
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required

@login_required
def editTaskPredeterminate(request, taskId):
    
    # Get the observation to edit
    task = get_object_or_404(TaskPredeterminate, pk=taskId)
    
    if request.method == 'POST':
        # If the form is submitted with data, process the form data
        form = createNewTaskPredeterminate.CreateNewTaskPredeterminate(request.POST, instance=task)
        if form.is_valid():
            
            task = form.save(user=request.user, commit=False)
            
            # Save the updated task to the database
            task.save()
    
            # Redirect to the viewTaskPredeterminate page
            return redirect('viewTaskPredeterminate')
    else:
        # If it's a GET method, render the edit form with the current task data
        form = createNewTaskPredeterminate.CreateNewTaskPredeterminate(instance=task)
    
    # Render the edit form
    return render(request, 'editTaskPredeterminate.html', {'form': form})
