from django.db import models
from django.contrib.auth.models import User


STATUS = ((0, "Confirmed"), (1, "Cancelled"))


TIME_CHOICES = (
    ("08:00", "08:00"),
    ("09:00", "09:00"),
    ("10:00", "10:00"),
    ("11:00", "11:00"),
    ("12:00", "12:00"),
    ("13:00", "13:00"),
    ("14:00", "14:00"),
    ("15:00", "15:00"),
    ("16:00", "16:00"),
    ("17:00", "17:00"),
    ("18:00", "18:00"),
    ("19:00", "19:00"),
)


# Create your models here.
class Appointment(models.Model):
    """
    Appointment Booking model
    """
    customer = models.ForeignKey(
        User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=35, null=True, blank=True)
    last_name = models.CharField(max_length=35, null=True, blank=True)
    phone = models.CharField(max_length=15, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    date = models.DateField()
    time = models.CharField(max_length=5, choices=TIME_CHOICES,
                            default="08:00")
    status = models.IntegerField(choices=STATUS, default=0)
