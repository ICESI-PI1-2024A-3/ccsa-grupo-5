from itertools import chain
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from .forms import *
from django.db import transaction
from .models import *
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required




# Create your views here.
@login_required
def index(request):
    return render(request, 'index.html')
@login_required
def selectTypePetition(request):
    return render(request, 'selectTypePetition.html')
        

@login_required
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

@login_required
def createOther(request):
    if request.method == 'POST':
        form = CreateNewOtherPetition(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = CreateNewOtherPetition()
    return render(request, 'createOther.html', {'form': form})

@login_required
def viewPetition(request):
    monitorings = Monitoring.objects.all()
    others = Other.objects.all()
    petitions = list(chain(monitorings, others))
    return render(request, 'viewPetition.html', {
        'petitions': petitions
    })
    
@login_required
def showPetition(request, petitionId):
    solicitud = None
    
    # Intenta obtener la solicitud como Other
    try:
        solicitud = Other.objects.get(pk=petitionId)
        observations = Observation.objects.filter(petition=solicitud)
        return render(request, 'viewPetitionO.html', {'solicitud': solicitud, 'observations': observations, 'petitionId': petitionId})
    except Other.DoesNotExist:
        pass
    
    # Si no es una solicitud de Other, intenta obtenerla como Monitoring
    try:
        solicitud = Monitoring.objects.get(pk=petitionId)
        observations = Observation.objects.filter(petition=solicitud)
        return render(request, 'viewPetitionM.html', {'solicitud': solicitud, 'observations': observations, 'petitionId': petitionId})
    except Monitoring.DoesNotExist:
        pass
    
    # Si no se encuentra la solicitud, renderiza una plantilla de error o maneja el caso según sea necesario
    return render(request, 'error.html', {'mensaje': 'La solicitud no se encuentra'})


@login_required
def deletePetition(request, petitionId):
    petition = get_object_or_404(Petition, pk=petitionId)
    
    if request.method == 'POST':
        petition.delete()
        return redirect('viewPetition')
        

@login_required
def rejectPetition(request, petitionId):
    
    petition = Petition.objects.get(pk=petitionId)
    if request.method == 'POST':
        if 'rechazar' in request.POST:  # Verifica si se hizo clic en el botón "Rechazar"
            petition.state = 'rechazado'
            petition.save()
            return redirect('showPetition', petitionId=petitionId)  # Redirigir a la página de detalles de la solicitud
        elif 'cancelar' in request.POST:  # Verifica si se hizo clic en el botón "Cancelar"
            return redirect('showPetition', petitionId=petitionId)  # Redirigir a la página de detalles de la solicitud
    return render(request, 'rejectPetition.html')

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

@login_required
def deleteObservation(request, observationId):
    petition = get_object_or_404(Observation, pk=observationId)
    
    if request.method == 'POST':
        petition.delete()
        return redirect('viewPetition')


@login_required
def editObservation(request, petitionId, observationId):
    # Obtener la observación a editar
    observation = get_object_or_404(Observation, pk=observationId)
    
    if request.method == 'POST':
        # Si el formulario se envió con datos, procesar los datos del formulario
        form = CreateNewObservation(request.POST, instance=observation)
        if form.is_valid():
            # Obtener la instancia de la observación pero no guardarla todavía
            observation = form.save(commit=False)
            
            # Asignar la ID de la petición a la observación
            observation.petition_id = petitionId
            
            # Guardar la observación actualizada en la base de datos
            observation.save()
    
            # Redirigir a la página de detalles de la solicitud
            return redirect('showPetition', petitionId=petitionId)
    else:
        # Si es un método GET, renderizar el formulario de edición con los datos de la observación actual
        form = CreateNewObservation(instance=observation)
    
    # Renderizar el formulario de edición
    return render(request, 'editObservation.html', {'form': form})

@login_required
def assignUserToPetition(request, petitionId):
    petition = Petition.objects.get(pk=petitionId)
    if request.method == 'POST':
        if 'assign' in request.POST:  # Verifica si se hizo clic en el botón "Rechazar"
            user_id = request.POST['user']
            user = User.objects.get(pk=user_id)
            petition.user = user
            petition.save()
            return redirect('showPetition', petitionId=petitionId)  # Redirigir a la página de detalles de la solicitud
        elif 'cancel' in request.POST:  # Verifica si se hizo clic en el botón "Cancelar"
            return redirect('showPetition', petitionId=petitionId)  # Redirigir a la página de detalles de la solicitud
        
    else:
        users = User.objects.all()  # Obtén todos los usuarios registrados
        return render(request, 'assignUserToPetition.html', {'petition': petition, 'users': users})