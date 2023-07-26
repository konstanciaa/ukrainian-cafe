from django.contrib import admin
from django.contrib.admin import ModelAdmin
from .models import Booking, Specials
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Booking)
class BookingAdmin(ModelAdmin):
    """
    Class registered to represent booking model
    in admin database.
    """
    list_display = ('user', 'first_name', 'last_name', 'phone',
                    'email', 'booking_date', 'time', 'guests')
    search_fields = ['first_name', 'last_name', 'booking_date', 'time',
                     'phone']
    list_filter = ('last_name', 'booking_date', 'time')


@admin.register(Specials)
class SpecialsAdmin(SummernoteModelAdmin):
    """
    Class registered to represent today's specials
    model in admin database.
    """
    list_display = ('title', 'slug', 'description', 'image', 'today')
    search_fields = ['title',  'slug']
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('description')
