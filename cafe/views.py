from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic, View
from .models import Booking, Specials
from .forms import BookingForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required


class SpecialsView(generic.ListView):
    model = Specials
    queryset = Specials.objects.filter(today=True)
    template_name = 'index.html'


@login_required
def add_booking(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save()
            booking.user = request.user
            booking.save()
            messages.success(request, 'Booking successful.')
            return redirect('view_booking')
        else:
            messages.error(request, 'Booking date must be in the future.')
    form = BookingForm()
    context = {
        'form': form
    }
    return render(request, 'add_booking.html', context)


@login_required
def view_booking(request):
    bookings = Booking.objects.filter(user__in=[request.user])
    context = {
        'bookings': bookings
    }
    return render(request, 'view_booking.html', context)


@login_required
def edit_booking(request, booking_id):
    book = get_object_or_404(Booking, id=booking_id)
    if request.method == "POST":
        form = BookingForm(request.POST, instance=book)
        if form.is_valid():
            booking = form.save()
            booking.user = request.user
            booking.save()
            messages.success(request, 'Your booking has been updated.')
        return redirect('view_booking')
    form = BookingForm(instance=book)
    context = {
        'form': form
    }
    return render(request, 'edit_booking.html', context)
