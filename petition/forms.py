from .models import Petition,Other,Monitoring 
from django import forms

#class CreateNewPetition(forms.Form):
class CreateNewMonitoringPetition(forms.ModelForm):
    class Meta:
        model = Monitoring
        fields = '__all__'
        
class EditState(forms.ModelForm):
    class Meta:
        model = Petition
        fields = ['state']
        
class CreateNewOtherPetition(forms.ModelForm):
    class Meta:
        model = Other
        fields = '__all__'
    
    


    def clean_archivo(self):
        archivo = self.cleaned_data.get('archivo')
        # Aquí puedes realizar validaciones adicionales si es necesario
        return archivo
        