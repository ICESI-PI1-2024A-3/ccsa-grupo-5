from itertools import chain
from django.http import HttpResponse, JsonResponse
from django.core.serializers import serialize
from django.shortcuts import get_object_or_404, redirect, render
from ..forms import *
from django.db import transaction
from ..models import *
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required





@login_required
def deleteObservation(request, observationId):
    petition = get_object_or_404(Observation, pk=observationId)
    
    if request.method == 'POST':
        petition.delete()
        return redirect('viewPetition')