from ..models import *
from django import forms

class CreateNewObservation(forms.ModelForm):
    """
    Form for creating a new observation.
    """

    petitionId = None  # Additional attribute to store the ID of the petition

    class Meta:
        model = Observation
        exclude = ["date", "time", "petition", "author"]

    def save(self, user, commit=True):
        """
        Save the form instance.
        """
        observation = super(CreateNewObservation, self).save(commit=False)
        observation.author = f"{user.first_name} {user.last_name}"  # Set the name of the current User
        observation.date = timezone.now().date()  # Set the current date
        observation.time = timezone.localtime()  # Set the current time
        observation.petition_id = self.petitionId  # Assign the ID of the petition
        if commit:
            observation.save()
        return observation
