from ..models import *
from django import forms

class CreateNewTask(forms.ModelForm):
    """
    Form for creating a new task.
    """
    petitionId = None  # Additional attribute to store the ID of the petition
    
    class Meta:
        model = Task
        exclude = ["isComplete", "petition"]
    def save(self, user, commit=True):
        """
        Save the form instance.
        """
        task = super(CreateNewTask, self).save(commit=False)
        task.petition_id = self.petitionId  # Set the current User
        if commit:
            task.save()
        return task
