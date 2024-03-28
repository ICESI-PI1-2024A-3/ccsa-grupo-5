from itertools import chain
from django.http import HttpResponse, JsonResponse
from django.core.serializers import serialize
from django.shortcuts import get_object_or_404, redirect, render
from ..forms import createNewOtherPetition
from django.db import transaction
from ..models import *
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required







@login_required
def createOther(request):
    if request.method == 'POST':
        form = createNewOtherPetition.CreateNewOtherPetition(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('viewPetition')
    else:
        form = createNewOtherPetition.CreateNewOtherPetition()
    return render(request, 'createOther.html', {'form': form})