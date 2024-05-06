"""
View function to create a new task predeterminate.
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
from login.permissions import groupRequired

@login_required
@groupRequired('Admin')
def createTaskPredeterminate(request):
    
    if request.method == 'POST':
        form = createNewTaskPredeterminate.CreateNewTaskPredeterminate(request.POST)
        if form.is_valid():
            form.save(user=request.user)
            return redirect('viewTaskPredeterminate')
    else:
        form = createNewTaskPredeterminate.CreateNewTaskPredeterminate()
    return render(request, 'createTaskPredeterminate.html', {'form': form})
