from .models import Petition,Other,Monitoring 
from django import forms

#class CreateNewPetition(forms.Form):
class CreateNewMonitoringPetition(forms.ModelForm):
    class Meta:
        model = Monitoring
        fields = '__all__'
        
class CreateNewOtherPetition(forms.ModelForm):
    class Meta:
        model = Other
        fields = '__all__'
