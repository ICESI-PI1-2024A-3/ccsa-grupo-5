from ..models import *
from django import forms


class CreateNewObservation(forms.ModelForm):
    petitionId = None  # Atributo adicional para almacenar la ID de la petición

    class Meta:
        model = Observation
        exclude = ["date", "time", "petition", "author"]

    def save(self, user, commit=True):
        observation = super(CreateNewObservation, self).save(commit=False)
        observation.author = f"{user.first_name} {user.last_name}"  # Establecer el nombre del Usuario actual
        observation.date = timezone.now().date()  # Establecer la fecha actual
        observation.time = timezone.localtime()  # Establecer la hora actual
        observation.petition_id = self.petitionId  # Asignar la ID de la petición
        if commit:
            observation.save()
        return observation
