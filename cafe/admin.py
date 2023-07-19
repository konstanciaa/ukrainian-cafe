from django.contrib import admin
from .models import Customer, Booking, Specials
from django_summernote.admin import SummernoteModelAdmin


# Customers
@admin.register(Customer)
class CustomerAdmin(SummernoteModelAdmin):

    list_display = ('user', 'first_name', 'last_name', 'phone',
                    'email')
    search_fields = ['user',  'phone', 'email', 'last_name']


# Bookings
@admin.register(Booking)
class BookingAdmin(SummernoteModelAdmin):

    list_display = ('id', 'first_name', 'last_name', 'date',
                    'time', 'guests', 'booking_status') 
    search_fields = ['id', 'last_name', 'date', 'time',
                     'booking_status']
    list_filter = ('booking_status', 'date')
    actions = ['confirm_booking']

    def confirm_booking(self, request, queryset):
        queryset.update(confirmed=True)


# Specials
@admin.register(Specials)
class SpecialsAdmin(SummernoteModelAdmin):

    list_display = ('title', 'slug', 'description', 'image', 'today')
    search_fields = ['title',  'description']
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('description')
