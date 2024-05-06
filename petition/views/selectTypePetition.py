"""
View function to render the page for selecting the type of petition.
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

@login_required
@groupRequired('Admin', 'Lider de Proceso')
def selectTypePetition(request):
    """
    Render a page for selecting the type of petition.

    Renders the 'selectTypePetition.html' template, accessible only to users
    with 'Admin' or 'Lider de Proceso' permissions.

    Args:
        request: HttpRequest object.

    Returns:
        Rendered selectTypePetition.html template.
    """
    return render(request, 'selectTypePetition.html')