import datetime
from .models import UserProfile, Booking, TABLE_TYPE, TIME_SLOTS
from django import forms
from django.forms import ModelForm, CheckboxSelectMultiple, TextInput, NumberInput
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django_summernote.widgets import SummernoteWidget


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ('table_type','booking_date','time','num_of_guests',)
    
