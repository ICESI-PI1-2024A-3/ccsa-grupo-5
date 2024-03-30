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


@groupRequired('Admin', 'Lider de Proceso')
@login_required
def viewPetitionWithoutUser(request):
    
    monitorings = Monitoring.objects.filter(user=None)
    others = Other.objects.filter(user=None)
    
    petitions = list(chain(monitorings, others))

    return render(request, 'viewPetitionWithoutUser.html', {
           'petitions': petitions
    })