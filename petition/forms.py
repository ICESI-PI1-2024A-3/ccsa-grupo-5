from .models import *
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
    
class CreateNewObservation(forms.ModelForm):
    petition_id = None  # Atributo adicional para almacenar la ID de la petición

    class Meta:
        model = Observation
        exclude = ['date', 'time', 'petition']

    def save(self, commit=True):
        observation = super(CreateNewObservation, self).save(commit=False)
        observation.date = timezone.now().date()  # Establecer la fecha actual
        observation.time = timezone.now().time()  # Establecer la hora actual
        observation.petition_id = self.petition_id  # Asignar la ID de la petición
        if commit:
            observation.save()
        return observation
        
        