"""
View function to delete an task predeterminate.
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

@login_required
def deleteTaskPredeterminate(request, taskId):
    task = get_object_or_404(TaskPredeterminate, pk=taskId)
    if request.method == 'POST':
        if "eliminar" in request.POST:
            task.delete()
            return redirect("viewTaskPredeterminate")
        elif "cancelar" in request.POST:
            return redirect("viewTaskPredeterminate")
        
    return render(request, "deleteTask.html", {"task": task})
