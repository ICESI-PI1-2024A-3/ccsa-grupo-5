from itertools import chain
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from .forms import CreateNewMonitoringPetition, CreateNewOtherPetition
from django.db import transaction
from .models import *



# Create your views here.
def index(request):
    return render(request, 'index.html')

def selectTypePetition(request):
    return render(request, 'selectTypePetition.html')
        
        
@transaction.atomic
def createMonitoring(request):
    if request.method == 'POST':
        form = CreateNewMonitoringPetition(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = CreateNewMonitoringPetition()
    return render(request, 'createMonitoring.html', {'form': form})

def createOther(request):
    if request.method == 'POST':
        form = CreateNewOtherPetition(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = CreateNewOtherPetition()
    return render(request, 'createOther.html', {'form': form})

def petitions(request):
    monitorings = Monitoring.objects.all()
    others = Other.objects.all()
    petitions = list(chain(monitorings, others))
    return render(request, 'petitions.html', {
        'petitions': petitions
    })
    

def editPetition(request, solicitudId):
    solicitud = None
    
    # Intenta obtener la solicitud como Other
    try:
        solicitud = Other.objects.get(pk=solicitudId)
        return render(request, 'editPetitionO.html', {'solicitud': solicitud})
    except Other.DoesNotExist:
        pass
    
    # Si no es una solicitud de Other, intenta obtenerla como Monitoring
    try:
        solicitud = Monitoring.objects.get(pk=solicitudId)
        return render(request, 'editPetitionM.html', {'solicitud': solicitud})
    except Monitoring.DoesNotExist:
        pass
    
    # Si no se encuentra la solicitud, renderiza una plantilla de error o maneja el caso según sea necesario
    return render(request, 'error.html', {'mensaje': 'La solicitud no se encuentra'})
