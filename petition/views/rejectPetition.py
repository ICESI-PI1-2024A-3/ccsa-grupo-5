from itertools import chain
from django.http import Http404, HttpResponse, JsonResponse
from django.core.serializers import serialize
from django.shortcuts import get_object_or_404, redirect, render
from ..forms import *
from django.db import transaction
from ..models import *
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required


@login_required
def rejectPetition(request, petitionId):

    try:
        petition = Petition.objects.get(pk=petitionId)
    except Petition.DoesNotExist:
        # Si no se encuentra la solicitud, lanza un error 404
        raise Http404("La solicitud no se encuentra")

    if request.method == "POST":
        if (
            "rechazar" in request.POST
        ):  # Verifica si se hizo clic en el botón "Rechazar"
            petition.state = "rechazado"
            petition.save()
            return redirect(
                "showPetition", petitionId=petitionId
            )  # Redirigir a la página de detalles de la solicitud
        elif (
            "cancelar" in request.POST
        ):  # Verifica si se hizo clic en el botón "Cancelar"
            return redirect(
                "showPetition", petitionId=petitionId
            )  # Redirigir a la página de detalles de la solicitud
    return render(request, "rejectPetition.html")
