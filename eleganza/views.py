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
    Form is saved if inputs are valid and user is
    redirected to his/her profile page.
    """
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        appointment = form.save(commit=False)
        if form.is_valid():
            appointment.customer = request.user
            appointment.save()
            messages.success(
                request, f'Thank you! We look forward to seeing you.')
            return redirect('my_profile')
    form = AppointmentForm()
    context = {
        'form': form
    }
    return render(request, 'book.html', context)


def edit_booking(request, appointment_id):
    """
    A view to edit an existing booking.
    Form is saved if inputs are valid and user is
    redirected to his/her profile page.
    """
    # get a copy of the appointment record from db
    appointment = get_object_or_404(Appointment, id=appointment_id)
    if request.method == 'POST':
        form = AppointmentForm(request.POST, instance=appointment)
        appointment = form.save(commit=False)
        if form.is_valid():
            appointment.customer = request.user
            appointment.save()
            return redirect('my_profile')
    form = AppointmentForm(instance=appointment)
    context = {
        'form': form
    }
    return render(request, 'edit_booking.html', context)


def cancel_booking(request, appointment_id):
    """
    A view to delete an existing booking.
    User is redirected to his/her profile page.
    """
    # get a copy of the appointment record from db
    appointment = get_object_or_404(Appointment, id=appointment_id)
    appointment.delete()
    return redirect('my_profile')
