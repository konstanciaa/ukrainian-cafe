from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic, View
from .models import Booking, Specials
from .forms import BookingForm, SpecialsForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required


class SpecialsView(generic.ListView):
    model = Specials
    queryset = Specials.objects.filter(today="yes")
    template_name = 'index.html'


@login_required
def add_specials(request):
    if request.user.is_superuser:
        if request.method == 'POST':
            form = SpecialsForm(request.POST, request.FILES)
            if form.is_valid():
                specials = form.save()
                specials.save()
                messages.success(request, 'You have successfully added a new item.')
            else:
                print(form.errors)
            return redirect('today_specials')

        form = SpecialsForm()
        context = {
            'form': form
        }
        return render(request, 'add_specials.html', context)


@login_required
def view_specials(request):
    if request.user.is_superuser:
        specials = Specials.objects.all()
        context = {
            'specials': specials
        }
        return render(request, 'today_specials.html', context)


@login_required
def edit_specials(request, special_id):
    item = get_object_or_404(Specials, id=special_id)
    if request.method == "POST":
        form = SpecialsForm(request.POST, instance=item)
        if form.is_valid():
            specials = form.save()
            specials.save()
            messages.success(request, 'An item has been updated.')
        return redirect('today_specials')
    form = SpecialsForm(instance=item)
    context = {
        'form': form
    }
    return render(request, 'edit_specials.html', context)


@login_required
def delete_specials(request, special_id):
    item = get_object_or_404(Specials, id=special_id)
    if request.method == "POST":
        form = SpecialsForm(request.POST, instance=item)
        if item.delete():
            messages.success(request, 'The item has been deleted.')
            return redirect('today_specials')

    form = SpecialsForm(instance=item)
    context = {
        'form': form
    }
    return render(request, 'delete_specials.html', context)


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
    if request.user.is_superuser:
        bookings = Booking.objects.all()
        context = {
            'bookings': bookings
        }
        return render(request, 'view_booking.html', context)
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


@login_required
def delete_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    if request.method == "POST":
        form = BookingForm(request.POST, instance=booking)
        if booking.delete():
            messages.success(request, 'Your booking has been deleted.')
            return redirect('view_booking')

    form = BookingForm(instance=booking)
    context = {
        'form': form
    }
    return render(request, 'delete_booking.html', context)
