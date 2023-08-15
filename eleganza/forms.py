import datetime
from django import forms
from .models import Appointment


class DateInput(forms.DateInput):
    """
    Class to show datepicker,
    code written with help from my Mentor Malia Havlicek
    """
    input_type = 'date'


class AppointmentForm(forms.ModelForm):
    class Meta:
        """ inner class to define which model the form is associated with """
        model = Appointment
        fields = ['first_name', 'last_name', 'phone', 'email', 'date', 'time']

        # code written with help from my Mentor Malia Havlicek
        widgets = {
            'date': DateInput(attrs={
                'min': datetime.date.today()+datetime.timedelta(days=0),
                'max': datetime.date.today()+datetime.timedelta(days=30)}),
        }
