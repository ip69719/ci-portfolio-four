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

    def clean(self):
        """
        Method used for multi-field custom validation.
        Code to display field specific validation errors adopted from
        GeeksforGeeks tutorial:
        https://www.geeksforgeeks.org/python-form-validation-using-django/

        The code to check if appointment conflict exists was written by
        my Mentor Malia Havlicek
        """
        # data from the form is fetched using super function
        cleaned_data = super().clean()

        # get the user submitted inputs
        first_name = cleaned_data.get("first_name")
        last_name = cleaned_data.get("last_name")
        phone = cleaned_data.get("phone")
        date = self.cleaned_data.get("date")
        time = self.cleaned_data.get("time")

        # this code to check conflicts was written by my Mentor Malia Havlicek
        conflicts = Appointment.objects.filter(date=date).filter(time=time).exclude(pk=self.instance.pk)  # noqa
        if conflicts.exists():
            raise forms.ValidationError(
                "This appointment conflicts with an existing appointment.")

        # condition to be met for the first_name field
        if len(first_name) < 2:
            self._errors['first_name'] = self.error_class(
                ['First name should be at least two characters long'])

        # condition to be met for the last_name field
        if len(last_name) < 2:
            self._errors['last_name'] = self.error_class(
                ['Last name should be at least two characters long'])

        # condition to be met for the phone field (length)
        if len(phone) < 8:
            # https://en.wikipedia.org/wiki/Telephone_numbers_in_the_Republic_of_Ireland
            self._errors['phone'] = self.error_class(
                ['Please enter a valid phone number. It should contain at least 8 digits.'])  # noqa:E501

        # condition to be met for the phone field (digits only)
        if not phone.isdigit():
            self._errors['phone'] = self.error_class(
                ['Please enter a valid phone number. It cannot contain letters or special characters.'])  # noqa:E501

        # check if time slot is in the past
        time_now = datetime.datetime.now()
        # extract time and convert it into datetime.time object
        time_now_str = datetime.datetime.strftime(time_now, '%H:%M')
        time_now_obj = datetime.datetime.strptime(time_now_str, '%H:%M').time()
        # convert time slot selected by the user into datetime.time object
        input_time_str = time
        input_time_obj = datetime.datetime.strptime(
            input_time_str, '%H:%M').time()
        # raise error if time slot selected is in the past
        if input_time_obj <= time_now_obj:
            self._errors['time'] = self.error_class(
                ['The time slot you selected is in the past'])

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
