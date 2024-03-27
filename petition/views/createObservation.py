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
def createObservation(request, petitionId):
    if request.method == 'POST':
        form = CreateNewObservation(request.POST)
        if form.is_valid():
            form.petition_id = petitionId 
            form.save()
            return redirect('showPetition', petitionId = petitionId )
    else:
        form = CreateNewObservation()
    return render(request, 'createObservation.html', {'form': form, 'petitionId': petitionId} )