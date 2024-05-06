"""
View function to handle rejecting a petition.
"""

from itertools import chain
from django.http import Http404, HttpResponse, JsonResponse
from django.core.serializers import serialize
from django.shortcuts import get_object_or_404, redirect, render
from ..forms import createNewObservation
from django.db import transaction
from ..models import *
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group

from django.db.models.signals import post_save
from notify.signals import notify
from notify.utils.models import notify_signals
from login.models import User

@login_required
def rejectPetition(request, petitionId):
    """
    Handle rejecting a petition.

    Retrieves the petition by its ID. If the petition is found,
    processes the rejection if a POST request is received.

    Args:
        request: HttpRequest object.
        petitionId: ID of the petition to reject.

    Returns:
        If a POST request is received:
            If "rechazar" button is clicked, updates petition state to "rechazado"
            and redirects to the showPetition page.
            If "cancelar" button is clicked, redirects to the showPetition page.
        If a GET request is received:
            Rendered rejectPetition.html template.
    
    Raises:
        Http404: If the petition is not found.
    """
    try:
        petition = Petition.objects.get(pk=petitionId)
    except Petition.DoesNotExist:
        raise Http404("La solicitud no se encuentra")

    if request.method == "POST":
        if "rechazar" in request.POST:
            # Update petition state to "rechazado" if "rechazar" button is clicked
            petition.state = "rechazado"
            petition.save()
            
            if 'Admin' in request.user.getGroup():
                # Notify to Manager
                notifyOne = petition.user
                
                #Notify to leader
                notifyTwo = petition.userAsigner
                
                if request.user in notifyTwo:
                    notifyTwo=notifyOne
                
            elif 'Lider de Proceso' in request.user.getGroup():
                # Notify to Manager
                notifyOne = petition.user
                
                #Notify to Admin
                notifyTwo = User.objects.filter(groups__name='Admin')
            else: # Is a Manager
                
                # Notify to Leader
                notifyOne = petition.userAsigner
                
                #Notify to Admin
                notifyTwo = User.objects.filter(groups__name='Admin')
                
                if notifyOne in notifyTwo:
                    notifyTwo=notifyOne
                
            if notifyOne == notifyTwo:
                # Notify to Manager
                notify.send(actor=request.user, destiny=notifyOne, verb="La solicitud "+str(petitionId)+" ha sido rechazada por "+str(request.user), level="success", sender=request.user)
                post_save.connect(notify_signals, sender=request.user)
            else:
                    
                # Notify to One
                notify.send(actor=request.user, destiny=notifyOne, verb="La solicitud "+str(petitionId)+" ha sido rechazada por "+str(request.user), level="success", sender=request.user)
                post_save.connect(notify_signals, sender=request.user)
                
                if isinstance(notifyTwo,list):
                    
                    for t in notifyTwo:
                        
                        #Notify to leader
                        notify.send(actor=request.user, destiny=t, verb="La solicitud "+str(petitionId)+" ha sido rechazada por "+str(request.user), level="success", sender=request.user)
                        post_save.connect(notify_signals, sender=request.user)
                else:
                    #Notify to leader
                        notify.send(actor=request.user, destiny=notifyTwo, verb="La solicitud "+str(petitionId)+" ha sido rechazada por "+str(request.user), level="success", sender=request.user)
                        post_save.connect(notify_signals, sender=request.user)
        
            
            return redirect("showPetition", petitionId=petitionId)
        elif "cancelar" in request.POST:
            # Redirect to showPetition page if "cancelar" button is clicked
            return redirect("showPetition", petitionId=petitionId)

    # Render rejectPetition.html template for GET requests
    return render(request, "rejectPetition.html")