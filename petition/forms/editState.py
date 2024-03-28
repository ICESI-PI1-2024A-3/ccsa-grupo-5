from ..models import *
from django import forms

class EditState(forms.ModelForm):
    class Meta:
        model = Petition
        fields = ['state']