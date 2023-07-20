from django.shortcuts import render, redirect
from django.views import generic, View
from .models import Booking, Specials, Customer
from .forms import BookingForm
from django.contrib.auth.models import User
from django.contrib import messages


# class BookingView(generic.ListView):
#     model = Booking
#     template_name = 'booking.html'


def booking(request):
    """
    renders booking page
    """
    if request.POST:
        form = BookingForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.customer = Customer.objects.get(user=request.user)
            instance.save()

        messages.success(request,
                        'Your booking request has been sent')
        return redirect('home')

    form = BookingForm(request.POST)
    return render(request, "booking.html", {'form': BookingForm})


class SpecialsView(generic.ListView):
    model = Specials
    queryset = Specials.objects.filter(today=True)
    template_name = 'index.html'
