import datetime
from django import forms
from .models import Appointment
from django.core.exceptions import ValidationError


class DateInput(forms.DateInput):
    """
    Class to show datepicker,
    code written with help from my Mentor Malia Havlicek
    """
    input_type = 'date'


class AppointmentForm(forms.ModelForm):
    """
    Function used for multi-field validation
    """
    def clean(self):

        # data from the form is fetched using super function
        cleaned_data = super().clean()

        # get the user submitted inputs
        first_name = cleaned_data.get("first_name")
        last_name = cleaned_data.get("last_name")

        # condition to be met for the first_name field
        if len(first_name) < 2:
            self._errors['first_name'] = self.error_class(
                ['First name should be at least two characters long'])

        # condition to be met for the lirst_name field
        if len(last_name) < 2:
            self._errors['last_name'] = self.error_class(
                ['Last name should be at least two characters long'])

        return cleaned_data

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
