from django import forms
from .models import Reminder

class DateInput(forms.DateInput):
    input_type = 'date'

class ReminderForm(forms.ModelForm):
    class Meta:
        model = Reminder
        fields = ['title', 'due_date', 'description']
        widgets = {
            'due_date': DateInput(),
        }

 




