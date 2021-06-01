"""
AppointmentsForm for djangoproject
https://simpleisbetterthancomplex.com/tutorial/2019/01/03/how-to-use-date-picker-with-django.html

"""
from django import forms
from appointments.models import appointments
from .widgets import FengyuanChenDatePickerInput


class AppointmentsForm(forms.ModelForm):

    class Meta:
        model = Appointments

        fields = [
            'user',
            'date',
        ]
        labels = {
            'user': 'Usuario',
            'date': 'Fecha',
        }
        widgets = {
            'user': forms.TextInput(attrs={'class':'form-control'}),
            'date': FengyuanChenDatePickerInput(),
        }
