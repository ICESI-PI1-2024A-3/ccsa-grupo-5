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
def viewPetition(request):
       
       if request.user.getGroup() == 'Admin':
              monitorings = Monitoring.objects.all()
              others = Other.objects.all()
              
       elif request.user.getGroup() == 'Lider de Proceso':
              monitorings = Monitoring.objects.filter(userAsigner = request.user)
              others = Other.objects.filter(userAsigner = request.user)    
       else:
              monitorings = Monitoring.objects.filter(user = request.user)
              others = Other.objects.filter(user = request.user)  


       petitions = None

       if monitorings.exists() or others.exists():
              petitions = list(chain(monitorings, others))

       return render(request, 'viewPetition.html', {
              'petitions': petitions
       })