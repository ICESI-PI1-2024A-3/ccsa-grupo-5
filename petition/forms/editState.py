from ..models import *
from django import forms

class EditState(forms.ModelForm):
    """
    Form for editing the state of a petition.
    """

    class Meta:
        model = Petition
        fields = ['state']
