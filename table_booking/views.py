from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.views import generic, View
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Booking, UserProfile
from .forms import BookingForm, SignUpForm, EditProfileForm
from django.contrib import messages
from django.contrib.auth.models import User


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

# def book(request, template_name="book.html"):
#     return render(
#         request, template_name,
#         {
#             "booking_form": booking_form
#         }
#     )

def booking_form(request):

    template_name = 'book.html'
    form = BookingForm(data=request.POST)
    
    if request.method == 'POST':        
        
        if form.is_valid():
            print('form is valid')
            booking = form.save(commit=False)
            booking.user = request.user
            booking.save()
            messages.success(request, 'Thank you! Your booking has been saved! You can access it through "My Profile" page.')
            return redirect('home')
        else:
            print('form is not valid')
            messages.error(request, form.errors)
            return redirect(booking_form)

    return render(
                request, template_name, {'form': form},
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

    try:
        user.delete()
        messages.success(request, 'Your account has been deleted successfully!')
        return redirect('home')
    except Exception as e: 
        messages.error(request, 'Oops! Something went wrong!')
        return redirect('home')