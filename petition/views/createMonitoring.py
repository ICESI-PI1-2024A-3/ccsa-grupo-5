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


@groupRequired('Admin', 'Lider de Proceso')
@login_required
@transaction.atomic
def createMonitoring(request):
    if request.method == 'POST':
        form = createNewMonitoringPetition.CreateNewMonitoringPetition(request.POST, request.FILES)
        if form.is_valid():
            form.save(request.user)
            return redirect('viewPetition')
    else:
        form = createNewMonitoringPetition.CreateNewMonitoringPetition()
    return render(request, 'createMonitoring.html', {'form': form})

