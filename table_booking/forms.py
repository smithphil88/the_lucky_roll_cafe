import datetime
from .models import UserProfile, Booking, TABLE_TYPE, TIME_SLOTS
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm, CheckboxSelectMultiple, TextInput, NumberInput
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django_summernote.widgets import SummernoteWidget


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ('table_type','booking_date','time','num_of_guests',)
    

class SignUpForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields =('username', 'first_name', 'last_name','email', 'password1', 'password2')