from django import forms
from .models import Appointment


class AppointmentForm(forms.ModelForm):
    class Meta:
        """ inner class to define which model the form is associated with """
        model = Appointment
        fields = ['first_name', 'last_name', 'phone', 'email', 'date', 'time']
