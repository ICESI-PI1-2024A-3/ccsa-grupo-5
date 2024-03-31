from ..models import *
from django import forms
from django.contrib.auth.models import Group



class CreateNewMonitoringPetition(forms.ModelForm):
    statesChoices = [
        ("pendiente", "Pendiente"),
        ("en_proceso", "En Proceso"),
    ]

    # Filtrar las opciones para el campo 'state' en el formulario de la petición
    state = forms.ChoiceField(choices=statesChoices, label="Estado")

    class Meta:
        model = Monitoring
        exclude = ["userAsigner"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["user"].required = False
        
        # Filtrar las opciones del campo "user" para mostrar solo los usuarios que pertenecen al grupo "Gestor de Contratacion"
        gestor_group = Group.objects.get(name='Gestor de Contratacion')
        self.fields['user'].queryset = gestor_group.user_set.all()

    def save(self, actualUser, commit=True, *args, **kwargs):
        instance = super().save(commit=False, *args, **kwargs)
        user = self.cleaned_data.get("user")
        if user:
            instance.userAsigner = actualUser
        if commit:
            instance.save()
        return instance
