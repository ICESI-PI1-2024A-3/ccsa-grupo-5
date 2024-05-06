from itertools import chain
from django.http import HttpResponse, JsonResponse
from django.core.serializers import serialize
from django.shortcuts import get_object_or_404, redirect, render
from ..forms import createNewTaskPredeterminate
from django.db import transaction
from ..models import *
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required

def notifications(request):
    # Obtén todas las notificaciones ordenadas por fecha de manera descendente
    notifications = Notification.objects.all().order_by('-date', '-time')
    
    # Verifica si hay notificaciones
    if notifications.exists():
        # Convierte el queryset en una lista
        notifications = list(notifications)
    
    return render(request, 'viewNotifications.html', {'notifications': notifications})