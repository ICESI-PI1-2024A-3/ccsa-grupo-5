from ..models import *
from django import forms


class CreateNewMonitoringPetition(forms.ModelForm):
    statesChoices = [
        ("pendiente", "Pendiente"),
        ("en_proceso", "En Proceso"),
    ]

    # Filtrar las opciones para el campo 'state' en el formulario de la petición
    state = forms.ChoiceField(choices=statesChoices, label="Estado")

    class Meta:
        model = Monitoring
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["user"].required = False
