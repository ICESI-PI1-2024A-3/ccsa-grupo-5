"""
View function to display the tasks predetermined.
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
def viewTaskPredeterminate(request):
    try:
        tasks = TaskPredeterminate.objects.all()
        return render(request, 'viewTaskPredeterminate.html', {'tasks': tasks})
    except TaskPredeterminate.DoesNotExist:
        pass
    
    raise Http404('No fueron encontradas las tareas predeterminadas')