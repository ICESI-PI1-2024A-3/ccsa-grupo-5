from ..models import *
from django import forms

class CreateNewOtherPetition(forms.ModelForm):
    class Meta:
        model = Other
        exclude = ['userAsigner']
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['user'].required = False
    
    def clean_archivo(self):
        archivo = self.cleaned_data.get('archivo')
        # Aquí puedes realizar validaciones adicionales si es necesario
        return archivo
    
    def save(self, actualUser, commit=True, *args, **kwargs):
        instance = super().save(commit=False, *args, **kwargs)
        user = self.cleaned_data.get('user')
        if user:
            instance.userAsigner = actualUser
        if commit:
            instance.save()
        return instance