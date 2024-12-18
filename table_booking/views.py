from django.shortcuts import render
from django.views import generic
from .models import Booking
from .forms import BookingForm

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