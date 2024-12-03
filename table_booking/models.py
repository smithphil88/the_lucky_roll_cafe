from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Booking(models.Model):
    num_of_guests = models.PositiveIntegerField()
    booked_on = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    additional_message = models.TextField()
