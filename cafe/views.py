from django.shortcuts import render
from django.views import generic, View
from .models import Booking, Specials


class BookingView(generic.ListView):
    model = Booking
    template_name = 'booking.html'


class SpecialsView(generic.ListView):
    model = Specials
    queryset = Specials.objects.filter(today=True)
    template_name = 'index.html'
