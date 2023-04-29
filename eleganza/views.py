from django.shortcuts import render
from .models import Appointment


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
