from django.contrib import admin
from django.contrib.admin import ModelAdmin
from .models import Booking, Specials
from django_summernote.admin import SummernoteModelAdmin


# Customers
# @admin.register(Customer)
# class CustomerAdmin(SummernoteModelAdmin):

#     list_display = ('user', 'first_name', 'last_name', 'phone',
#                     'email')
#     search_fields = ['user',  'phone', 'email', 'last_name']


# Bookings
@admin.register(Booking)
class BookingAdmin(ModelAdmin):

    list_display = ('user', 'first_name', 'last_name', 'phone',
                    'email', 'booking_date', 'time', 'guests')
    search_fields = ['first_name', 'last_name', 'booking_date', 'time',
                     'phone']
    list_filter = ('last_name', 'booking_date', 'time')
    # actions = ['confirm_booking']

    # def confirm_booking(self, request, queryset):
    #     queryset.update(confirmed=True)


# Specials
@admin.register(Specials)
class SpecialsAdmin(SummernoteModelAdmin):

    list_display = ('title', 'slug', 'description', 'image', 'today')
    search_fields = ['title',  'slug']
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('description')
