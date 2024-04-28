from ..models import *
from django import forms

class CreateNewTaskPredeterminate(forms.ModelForm):
    """
    Form for creating a new task predeterminate.
    """
    class Meta:
        model = TaskPredeterminate
        exclude = ["isComplete", "admin"]

    def save(self, user, commit=True):
        """
        Save the form instance.
        """
        taskPredeterminate = super(CreateNewTaskPredeterminate, self).save(commit=False)
        taskPredeterminate.admin = user  # Set the current User
        if commit:
            taskPredeterminate.save()
        return taskPredeterminate
