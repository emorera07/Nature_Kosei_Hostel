"""
AppointmentsForm for djangoproject
https://simpleisbetterthancomplex.com/tutorial/2019/01/03/how-to-use-date-picker-with-django.html

"""
from django import forms

from appointments.models import Event
#from .widgets import FengyuanChenDatePickerInput


class EventForm(forms.ModelForm):

    class Meta:
        model = Event()
        fields = [
            'user',
            'start_time',
            'end_time',
        ]
        labels = {
            'user': 'Usuario',
            'start_time': 'Fecha de inicio',
            'end_time': 'Fecha de fin',
        }
        widgets = {
            'user': forms.TextInput(attrs={'class':'form-control'}),
            'start_time': forms.DateInput(attrs={'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M'),
            'end_time': forms.DateInput(attrs={'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M'),
        }

"""
    def __init__(self, *args, **kwargs):
    super(EventForm, self).__init__(*args, **kwargs)
    # input_formats to parse HTML5 datetime-local input to datetime field
    self.fields['user'].max_length = 200
    self.fields['start_time'].input_formats = ('%Y-%m-%dT%H:%M',)
    self.fields['end_time'].input_formats = ('%Y-%m-%dT%H:%M',)
"""
