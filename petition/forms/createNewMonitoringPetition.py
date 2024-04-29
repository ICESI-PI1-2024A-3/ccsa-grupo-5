from ..models import *
from django import forms
from django.contrib.auth.models import Group



class CreateNewMonitoringPetition(forms.ModelForm):
    """
    Form for creating a new monitoring petition.
    """
    class Meta:
        model = Monitoring
        exclude = ["userAsigner", "percentage", "state"]

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
        instance.state = "pendiente" # Set the state of the petition
        if user:
            instance.userAsigner = actualUser
            instance.state = "en_proceso"  # Set the state of the petition
        if commit:
            
            instance.save()
        return instance
