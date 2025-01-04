from django.urls import include, path
from django.contrib import admin
from . import views
from .views import UserRegisterView, UserEditView, MyBookingsViews,EditBookingsView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('book/', views.booking_form, name='book'),
    path('my_bookings/', MyBookingsViews.as_view(), name='my_bookings'),
    path('edit_my_bookings/<slug:slug>', EditBookingsView.as_view(), name='edit_my_bookings'),
    path('register/', UserRegisterView.as_view(), name='register'),
    path('my_profile/', UserEditView.as_view(), name='my_profile'),
    path('delete-account/', views.delete_account, name='deleteaccount'),
]