from .models import Booking
from django import forms


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ('table_type','booking_date','time','num_of_guests',)
    


# class ProfileForm(ModelForm):