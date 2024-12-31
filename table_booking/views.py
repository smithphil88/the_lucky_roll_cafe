from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic, View
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from .models import Booking
from .forms import BookingForm, SignUpForm, EditProfileForm
from django.contrib import messages
from django.contrib.auth.models import User

booking_form = BookingForm()

# Create your views here.

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
    form_class = SignUpForm
    template_name = 'account/signup.html'
    success_url = reverse_lazy('account_login')

class UserEditView(generic.UpdateView):
    form_class = EditProfileForm
    template_name = 'edit_profile.html'
    success_url = reverse_lazy('home')

    def get_object(self):
        return self.request.user


@login_required
def delete_account(request):

    user = get_object_or_404(User, id=request.user.id)
    profile = User.objects.all()

    try:
        profile.delete()
        user.delete()
        messages.success(request, 'Your account has been deleted successfully!')
        return redirect('home')
    except Exception as e: 
        messages.error(request, 'Oops! Something went wrong!')
        return redirect('home')