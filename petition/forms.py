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
        exclude = ['rutAttachment']  # Excluye el campo rutAttachment del formulario

    archivo = forms.FileField(label='Archivo adjunto', help_text='Seleccione un archivo', required=False )
    
    def __init__(self, *args, **kwargs):
        super(CreateNewOtherPetition, self).__init__(*args, **kwargs)
        # Puedes personalizar los atributos del campo archivo aquí si es necesario
        self.fields['archivo'].widget.attrs.update({'class': 'createOther.html'})

    def clean_archivo(self):
        archivo = self.cleaned_data.get('archivo')
        # Aquí puedes realizar validaciones adicionales si es necesario
        return archivo

       