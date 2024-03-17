from .models import Petition,Other,Monitoring 
from django import forms

#class CreateNewPetition(forms.Form):
class CreateNewMonitoringPetition(forms.ModelForm):
    class Meta:
        model = Monitoring
        fields = '__all__'
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['user'].required = False
        
class EditState(forms.ModelForm):
    class Meta:
        model = Petition
        fields = ['state']
        
class CreateNewOtherPetition(forms.ModelForm):
    class Meta:
        model = Other
        fields = '__all__'
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['user'].required = False
    
    


    def clean_archivo(self):
        archivo = self.cleaned_data.get('archivo')
        # Aquí puedes realizar validaciones adicionales si es necesario
        return archivo
        