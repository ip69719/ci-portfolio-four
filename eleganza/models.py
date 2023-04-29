from django.db import models
from django.contrib.auth.models import User


STATUS = ((0, "Confirmed"), (1, "Cancelled"))


# Create your models here.
class Appointment(models.Model):
    """
    Appointment Booking model
    """
    customer = models.ForeignKey(
        User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=35)
    last_name = models.CharField(max_length=35)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    date = models.DateField()
    time = models.TimeField()
    status = models.IntegerField(choices=STATUS, default=0)
