from .models import Petition,Other,Monitoring 
from django import forms

#class CreateNewPetition(forms.Form):
class CreateNewPetition(forms.ModelForm):
    class Meta:
        model = Monitoring
        fields = '__all__'