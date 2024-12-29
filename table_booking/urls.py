from django.urls import include, path
from django.contrib import admin
from . import views
from .views import UserRegisterView, UserEditView

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('booking/', views.BookingList.as_view(), name='booking'),
    path('book/', views.book, name='book'),
    path('register/', UserRegisterView.as_view(), name='register'),
    path('edit_profile/', UserEditView.as_view(), name='edit_profile'),
]