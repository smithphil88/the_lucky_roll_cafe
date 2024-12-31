from django.urls import include, path
from django.contrib import admin
from . import views
from .views import UserRegisterView, UserEditView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('book/', views.book, name='book'),
    path('register/', UserRegisterView.as_view(), name='register'),
    path('edit_profile/', UserEditView.as_view(), name='edit_profile'),
    path('password/', auth_views.PasswordChangeView.as_view(template_name='account/password_reset.html')),
    path('delete-account/', views.delete_account, name='deleteaccount'),
]