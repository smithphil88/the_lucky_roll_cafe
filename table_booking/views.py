from django.shortcuts import render
from django.views import generic
from .models import Booking
# Create your views here.

class BookingList(generic.ListView):
    queryset = Booking.objects.filter(table_type=1).filter(num_of_guests=2)
    template_name = "bookings_list.html"


def home(request, template_name="index.html"):
    return render(
        request, template_name
    )

def about(request, template_name="about.html"):
    return render(
        request, template_name,
    )