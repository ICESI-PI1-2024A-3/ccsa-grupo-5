from ..models import *
from django import forms
from django.contrib.auth.models import Group



class CreateNewMonitoringPetition(forms.ModelForm):
    """
    Form for creating a new monitoring petition.
    """
    statesChoices = [
        ("pendiente", "Pendiente"),
        ("en_proceso", "En Proceso"),
    ]

    # Filter the options for the 'state' field in the petition form
    state = forms.ChoiceField(choices=statesChoices, label="Estado")

    class Meta:
        model = Monitoring
        exclude = ["userAsigner", "percentage"]

    def __init__(self, *args, **kwargs):
        """
        Initialize the form.
        """
        super().__init__(*args, **kwargs)
        self.fields["user"].required = False
        
        # Filter the options for the "user" field to show only users belonging to the "Gestor de Contratacion" group
        gestor_group = Group.objects.get(name='Gestor de Contratacion')
        self.fields['user'].queryset = gestor_group.user_set.all()

    def save(self, actualUser, commit=True, *args, **kwargs):
        """
        Save the form instance.
        """
        instance = super().save(commit=False, *args, **kwargs)
        user = self.cleaned_data.get("user")
        if user:
            instance.userAsigner = actualUser
        if commit:
            instance.save()
        return instance
