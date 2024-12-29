from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic, View
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from .models import Booking
from .forms import BookingForm
from django.contrib import messages
from django.contrib.auth.models import User

booking_form = BookingForm()

# Create your views here.

class BookingList(generic.ListView):
    queryset = Booking.objects.filter(table_type=1).filter(num_of_guests=2)
    template_name = "bookings_list.html"


def about(request, template_name="base.html"):
    return render(
        request, template_name,
    )

def home(request, template_name="index.html"):
    return render(
        request, template_name
    )

def about(request, template_name="about.html"):
    return render(
        request, template_name,
    )

def book(request, template_name="book.html"):
    return render(
        request, template_name,
        {
            "booking_form": booking_form
        }
    )

class UserRegisterView(generic.CreateView):
    form_class = UserCreationForm
    template_name = 'account/signup.html'
    success_url = reverse_lazy('account_login')
    
# class User