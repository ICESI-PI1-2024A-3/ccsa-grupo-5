from ..models import *
from django import forms

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