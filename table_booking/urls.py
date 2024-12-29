from django.urls import include, path
from django.contrib import admin
from . import views
from .views import UserRegisterView

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('booking/', views.BookingList.as_view(), name='booking'),
    path('book/', views.book, name='book'),
    # path('user-profile/', views.user_profile, name='userprofile'),
    path('register', UserRegisterView.as_view(), name='register')
]