from django.shortcuts import render
from .models import Appointment


# Create your views here.
def index(request):
    """ A view to return the index page """
    return render(request, 'index.html')


def all_appointments(request):
    """ A view to show all appointments """
    appointments = Appointment.objects.all()
    context = {
        'appointments': appointments,
    }
    return render(request, 'my_profile.html', context)
