import datetime
from django.utils import timezone
from .models import UserProfile, Booking, TABLE_TYPE, TIME_SLOTS
from django import forms
from django.core.exceptions import ValidationError
from datetime import date
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django_summernote.widgets import SummernoteWidget
from autoslug import AutoSlugField


class BookingForm(forms.ModelForm):
    booking_date = forms.DateField(widget=forms.SelectDateWidget(attrs={'class': 'form-select'}), required=True)
    time = forms.ChoiceField(choices=TIME_SLOTS,widget=forms.Select(attrs={'class': 'form-select'}), required=False)
    additional_message = forms.CharField(
        label='Please let us know if you have any other requirements',
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'rows': 4,
            'placeholder': 'Enter additional requirements here...',
            'style': 'resize: none;'
        }),
        required=False
    )
    table_type = forms.ChoiceField(choices=TABLE_TYPE, widget=forms.Select(attrs={'class': 'form-select'}), required=False)
    num_of_guests = forms.IntegerField(label="Guests (max-12 people)",
        widget=forms.NumberInput(attrs={'class': 'form-control', 'type': 'number', 'min': 1, 'max': 12, 'placeholder':'This field is required'}),
        required=True,
    )
    slug = AutoSlugField(max_length=70, unique=True)

    def clean_booking_date(self):
        booking_date = self.cleaned_data.get('booking_date')
        
        if booking_date is not None and booking_date < datetime.date.today():
            raise forms.ValidationError("Booking date cannot be in the past")
        
        return booking_date
    
    class Meta:
        model = Booking
        fields = ('table_type','booking_date','time', 'num_of_guests', 'additional_message')
        read_only = ['slug']

# class SignUpForm(UserCreationForm):
#     email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    
#     class Meta:
#         model = User
#         fields =('username', 'email', 'password1', 'password2')

#     def __init__(self, *args, **kwargs):
#         super(SignUpForm, self).__init__(*args, **kwargs)

#         self.fields['username'].widget.attrs['class'] = 'form-control'
#         self.fields['password1'].widget.attrs['class'] = 'form-control'
#         self.fields['password2'].widget.attrs['class'] = 'form-control'


class EditProfileForm(UserChangeForm):
    password = None
    first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control'}))
    
    class Meta:
        model = User
        fields =('username', 'email', 'first_name', 'last_name')


