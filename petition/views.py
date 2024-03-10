from django.http import HttpResponse
from django.shortcuts import redirect, render
from .forms import CreateNewPetition

# Create your views here.
def index(request):
    return render(request, 'index.html')

def selectTypePetition(request):
    return render(request, 'selectTypePetition.html')

def otro(request):
    return render(request, 'otro.html')
        
def createMoniroring(request):
    if request.method == 'POST':
        form = CreateNewPetition(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = CreateNewPetition()
    return render(request, 'createMonitoring.html', {'form': form})