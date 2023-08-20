from django.shortcuts import render, redirect, get_object_or_404
from .models import Appointment
from .forms import AppointmentForm
from django.contrib import messages


def index(request):
    """ A view to return the index page """
    return render(request, 'index.html')


def all_appointments(request):
    """
    A view to show all appointments.
    Returns appointment details for logged in user.
    """
    appointments = Appointment.objects.filter(customer=request.user)

    context = {
        'appointments': appointments,
        'appointment_form': AppointmentForm()
    }
    return render(request, 'my_profile.html', context)


def book(request):
    """
    A view to display the booking form to the user.
    Form is saved if inputs are valid and the user is redirected to his/her
    profile page. If user inputs are invalid then the entered booking details
    are displayed with validation errors.

    The else statement within the function was written with reference to
    GeeksforGeeks tutorial:
    https://www.geeksforgeeks.org/python-form-validation-using-django/
    """
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.customer = request.user
            appointment.save()
            messages.success(
                request, f'Thank you! We look forward to seeing you.')
            return redirect('my_profile')
        else:
            return render(request, 'book.html', {'form': form})
    else:
        form = AppointmentForm(None)
        context = {
            'form': form
            }
        return render(request, 'book.html', context)


def edit_booking(request, appointment_id):
    """
    A view to edit an existing booking. Displays form which is prefilled with
    existing appointment details that the User wants to edit.
    Form is saved if User inputs are valid. A confirmation message is
    displayed and the User is redirected to his/her profile page.
    If user inputs are invalid then the entered booking details
    are displayed on the form with validation errors.

    The else statement within the function was written with reference to
    GeeksforGeeks tutorial:
    https://www.geeksforgeeks.org/python-form-validation-using-django/
    """
    # get a copy of the appointment record from db
    appointment = get_object_or_404(Appointment, id=appointment_id)
    if request.method == 'POST':
        form = AppointmentForm(request.POST, instance=appointment)
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.customer = request.user
            appointment.save()
            messages.success(
                request, f'Your appointment has changed! We look forward to seeing you.')  # noqa:E501
            return redirect('my_profile')
        else:
            return render(request, 'edit_booking.html', {'form': form})
    else:
        form = AppointmentForm(instance=appointment)
        context = {
            'form': form
            }
        return render(request, 'edit_booking.html', context)


def cancel_booking(request, appointment_id):
    """
    A view to delete an existing booking.
    User is presented with a confirmation message and
    redirected to his/her profile page.
    """
    # get a copy of the appointment record from db
    appointment = get_object_or_404(Appointment, id=appointment_id)
    appointment.delete()
    messages.success(
        request, f'Appointment cancelled! We look forward to seeing you again soon.')  # noqa:E501
    return redirect('my_profile')


def error_500(request, *args, **argv):
    """
    Function to display custom error_500.html page
    """
    return render(request, 'error_500.html')


def error_404(request, exception):
    """
    Function to display custom error_404.html page
    """
    return render(request, 'error_404.html')
