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
def assignUserToPetition(request, petitionId):
    petition = Petition.objects.get(pk=petitionId)
    if request.method == 'POST':
        if 'assign' in request.POST:  # Verifica si se hizo clic en el botón "Rechazar"
            user_id = request.POST['user']
            user = User.objects.get(pk=user_id)
            petition.user = user
            
            petition.userAsigner = User.objects.get(pk=request.user.id)
            petition.save()
            return redirect('showPetition', petitionId=petitionId)  # Redirigir a la página de detalles de la solicitud
        elif 'cancel' in request.POST:  # Verifica si se hizo clic en el botón "Cancelar"
            return redirect('showPetition', petitionId=petitionId)  # Redirigir a la página de detalles de la solicitud
        
    else:
        users = User.objects.all()  # Obtén todos los usuarios registrados
        return render(request, 'assignUserToPetition.html', {'petition': petition, 'users': users})