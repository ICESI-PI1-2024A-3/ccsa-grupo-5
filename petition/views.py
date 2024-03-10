from django.http import HttpResponse
from django.shortcuts import redirect, render
from .forms import CreateNewMonitoringPetition, CreateNewOtherPetition

# Create your views here.
def index(request):
    return render(request, 'index.html')

def selectTypePetition(request):
    return render(request, 'selectTypePetition.html')
        
def createMonitoring(request):
    if request.method == 'POST':
        form = CreateNewMonitoringPetition(request.POST)
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