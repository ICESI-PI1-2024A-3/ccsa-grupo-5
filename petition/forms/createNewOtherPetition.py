from ..models import *
from django import forms
from django.contrib.auth.models import Group


class CreateNewOtherPetition(forms.ModelForm):
    """
    Form for creating a new other petition.
    """

    petitionDate = forms.DateField(
        widget=forms.DateInput(attrs={"type": "date"}), label="Fecha de solicitud"
    )
    startDate = forms.DateField(
        widget=forms.DateInput(attrs={"type": "date"}), label="Fecha de inicio"
    )
    endDate = forms.DateField(
        widget=forms.DateInput(attrs={"type": "date"}), label="Fecha de fin"
    )

    class Meta:
        model = Other
        exclude = ["userAsigner", "percentage", "state"]

    def __init__(self, *args, **kwargs):
        """
        Initialize the form.
        """
        super().__init__(*args, **kwargs)
        self.fields["user"].required = False

        # Filter options for the "user" field to display only users belonging to the "Gestor de Contratacion" group
        gestor_group = Group.objects.get(name="Gestor de Contratacion")
        self.fields["user"].queryset = gestor_group.user_set.all()

    def clean_archivo(self):
        """
        Clean the 'archivo' field.
        """
        archivo = self.cleaned_data.get("archivo")
        # You can perform additional validations here if necessary
        return archivo

    def clean(self):
        """
        Clean and validate form data.
        """
        cleaned_data = super().clean()
        startDate = cleaned_data.get("startDate")
        endDate = cleaned_data.get("endDate")
        petitionDate = cleaned_data.get("petitionDate")

        # Validate start and end date
        if startDate and endDate and startDate > endDate:
            self.add_error(
                "startDate",
                "La fecha de inicio no puede ser posterior a la fecha de fin.",
            )

        # Validate petition date
        if startDate and petitionDate and petitionDate > startDate:
            self.add_error(
                "petitionDate",
                "La fecha de la petición no puede ser posterior a la fecha de inicio.",
            )

        if endDate and petitionDate and petitionDate > endDate:
            self.add_error(
                "petitionDate",
                "La fecha de la petición no puede ser posterior a la fecha de fin.",
            )

        return cleaned_data

    def save(self, actualUser, commit=True, *args, **kwargs):
        """
        Save the form instance.
        """
        instance = super().save(commit=False, *args, **kwargs)
        instance.state = "pendiente"  # Set the state of the petition
        user = self.cleaned_data.get("user")
        if user:
            instance.userAsigner = actualUser
            instance.state = "en_proceso"  # Set the state of the petition
        if commit:
            instance.save()
        return instance
