import datetime
from .models import UserProfile, Booking, TABLE_TYPE, TIME_SLOTS
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django.forms import ModelForm, CheckboxSelectMultiple, TextInput, NumberInput
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django_summernote.widgets import SummernoteWidget
from autoslug import AutoSlugField


class BookingForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)

    booking_date = forms.DateField(widget=forms.DateInput(attrs={'class':'form-control', 'type':'date', 'value': datetime.date.today}), required=False)
    time = forms.ChoiceField(choices=TIME_SLOTS, required=False)
    additional_message = forms.CharField(max_length=200, widget=SummernoteWidget(), required=False)
    table_type = forms.ChoiceField(choices=TABLE_TYPE, required=False)
    # num_of_guests = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control', 'type':'number'}), required=False)
    num_of_guests = forms.IntegerField(label="Guests",
        widget=forms.NumberInput(attrs={'class': 'form-control', 'type': 'number', 'min': 1, 'max': 12}),
        required=False
    )
    slug = AutoSlugField(max_length=70, unique=True)
    
    class Meta:
        model = Booking
        fields = ('table_type','booking_date','time', 'num_of_guests', 'additional_message')
        read_only = ['slug']

class SignUpForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    
    class Meta:
        model = User
        fields =('username', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'


class EditProfileForm(UserChangeForm):
    password = None
    first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control'}))
    # favourite_game = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control'}))
    
    
    class Meta:
        model = User
        fields =('username', 'email', 'first_name', 'last_name',)

