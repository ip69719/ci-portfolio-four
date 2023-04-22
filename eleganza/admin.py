from django.contrib import admin
from .models import Appointment
# Register your models here.


@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('date', 'time', 'first_name', 'last_name',
                    'phone', 'email', 'status')
    search_fields = ['first_name', 'phone']
    list_filter = ('date', 'status')
