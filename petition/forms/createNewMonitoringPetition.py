from ..models import *
from django import forms

class CreateNewMonitoringPetition(forms.ModelForm):
    class Meta:
        model = Monitoring
        fields = '__all__'
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['user'].required = False