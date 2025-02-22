from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.views import generic, View
from django.views.generic.edit import UpdateView
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Booking, UserProfile
from .forms import BookingForm, EditProfileForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin


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


class UserEditView(generic.UpdateView):
    form_class = EditProfileForm
    template_name = 'my_profile.html'
    success_url = reverse_lazy('home')

    def get_object(self, queryset=None):
        return self.request.user

    def form_valid(self, form):
        messages.success(self.request, 'Your profile has been updated!')
        return super().form_valid(form)


@login_required
def delete_account(request):

    user = get_object_or_404(User, id=request.user.id)

    try:
        user.delete()
        messages.success(
            request, 'Your account has been deleted successfully!')
        return redirect('home')
    except Exception as e:
        messages.error(request, 'Oops! Something went wrong!')
        return redirect('home')


def booking_form(request):

    template_name = 'book.html'
    form = BookingForm(data=request.POST)
    slug = form.slug

    if request.method == 'POST':

        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.save()
            messages.success(
                request,
                'Thanks, you can see your booking on the "My Bookings" page.')
            return redirect('my_bookings')
        else:
            messages.error(request, form.errors)
            return redirect(booking_form)

    return render(
                request, template_name, {'form': form},
                )


class MyBookingsViews(View):

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            user = request.user
            user_bookings = Booking.objects.filter(user=user)
            template_name = "my_bookings.html"

            return render(
                request, template_name,
                {
                    "user_bookings": user_bookings
                    }
            )


class EditBookingsView(UpdateView, LoginRequiredMixin):

    model = Booking
    form_class = BookingForm
    template_name = 'edit_booking.html'
    success_url = reverse_lazy('my_bookings')

    def form_valid(self, form):
        form.instance.user = self.request.user
        response = super().form_valid(form)
        messages.success(
            self.request, 'Thank you! Your booking has been updated!')

        return response


def delete_booking(request, slug):

    booking = get_object_or_404(Booking, slug=slug)

    try:
        booking.delete()
        messages.warning(request, 'Your booking has been cancelled')

        return redirect('home')
    except Exception as e:
        messages.error(request, 'Oops! Something went wrong!')
        return redirect('home')
