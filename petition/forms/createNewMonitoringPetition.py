from ..models import *
from django import forms

class CreateNewMonitoringPetition(forms.ModelForm):
    class Meta:
        model = Monitoring
        exclude = ['userAsigner']
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['user'].required = False
        
    def save(self, actualUser, commit=True, *args, **kwargs):
        instance = super().save(commit=False, *args, **kwargs)
        user = self.cleaned_data.get('user')
        if user:
            instance.userAsigner = actualUser
        if commit:
            instance.save()
        return instance