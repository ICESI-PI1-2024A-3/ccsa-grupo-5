"""
View function to display petitions without assigned users.
"""

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
def viewPetitionWithoutUser(request):
    """
    Render a page displaying petitions without assigned users.

    Retrieves Monitoring and Other objects with no assigned users,
    combines them into a list of petitions, and renders a template
    displaying these petitions.

    Args:
        request: HttpRequest object.

    Returns:
        Rendered viewPetitionWithoutUser.html template with 'petitions' context.
    """
    monitorings = Monitoring.objects.filter(user=None)
    others = Other.objects.filter(user=None)
    
    petitions = list(chain(monitorings, others))

    return render(request, 'viewPetitionWithoutUser.html', {
           'petitions': petitions
    })