"""
Views to create application logic.
"""
from django.shortcuts import render, redirect, get_object_or_404
from django.db import IntegrityError
from django.views import generic, View
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Booking, Specials
from .forms import BookingForm, SpecialsForm

from django.contrib.auth.decorators import login_required


class SpecialsView(generic.ListView):
    """
    Creates view for today's specials on the home page
    """
    model = Specials
    queryset = Specials.objects.filter(today="yes")
    template_name = 'index.html'


@login_required
def add_specials(request):
    """
    Enables superuser to add new items to
    today's specials database.
    """
    if request.user.is_superuser:
        if request.method == 'POST':
            form = SpecialsForm(request.POST, request.FILES)
            if form.is_valid():
                specials = form.save()
                specials.save()
                messages.success(
                    request, 'You have successfully added a new item.'
                    )
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
    """
    Enables superuser to view all items in
    today's specials database.
    """
    if request.user.is_superuser:
        specials = Specials.objects.all()
        context = {
            'specials': specials
        }
        return render(request, 'today_specials.html', context)


@login_required
def edit_specials(request, special_id):
    """
    Enables superuser to edit items in
    today's specials database.
    """
    if request.user.is_superuser:
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
    """
    Enables superuser to delete items in
    today's specials database.
    """
    if request.user.is_superuser:
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
    """
    Enables user to make a booking
    and add it to the database.
    """
    if request.method == 'POST':
        form = BookingForm(request.POST)
        try:
            if form.is_valid():
                booking = form.save(commit=False)
                booking.user = request.user
                booking.save()
                messages.success(request, 'Booking successful.')
                return redirect('view_booking')
            else:
                messages.error(request, 'Booking date must be in the future.')
        except IntegrityError as e:
            if 'cafe_booking_user_id_first_name_last__25ede966_uniq' in str(e.args):
                messages.error(request, 'The booking already exists.')
                return redirect('home')
    form = BookingForm()
    context = {
        'form': form
    }
    return render(request, 'add_booking.html', context)


@login_required
def view_booking(request):
    """
    Enables user to view a booking after
    it has been made and added to the database.
    """
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
    """
    Enables user to edit a booking after
    it has been made and added to the database.
    """
    bookings = Booking.objects.filter(user__in=[request.user])
    book = get_object_or_404(bookings, id=booking_id)

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
    """
    Enables user to delete a booking after
    it has been made and added to the database.
    """
    bookings = Booking.objects.filter(user__in=[request.user])
    booking = get_object_or_404(bookings, id=booking_id)
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
