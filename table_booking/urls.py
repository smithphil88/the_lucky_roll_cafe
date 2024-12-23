from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('booking/', views.BookingList.as_view(), name='booking'),
    path('book/', views.book, name='book'),
    path('profile/', views.profile, name='profile')
]