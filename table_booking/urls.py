from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='base'),
    path('index/', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('booking/', views.BookingList.as_view(), name='home'),
]