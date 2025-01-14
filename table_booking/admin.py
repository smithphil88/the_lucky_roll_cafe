from django.contrib import admin
from .models import Booking, UserProfile
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Booking)
class BookingAdmin(SummernoteModelAdmin):
    list_display = (
        'user', 'table_type', 'booking_date', 'time',
        'num_of_guests', 'additional_message','slug')
    search_fields = ['user']
    list_filter = (
        'user', 'table_type', 'booking_date', 'time',
        'num_of_guests')
    summernote_fields = ('additional_message',)
