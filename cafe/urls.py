from . import views
from django.urls import path
# from .views import BookingView, SpecialsView
from .views import SpecialsView


urlpatterns = [
    path('', views.SpecialsView.as_view(), name='home'),
    path('add_booking/', views.add_booking, name='add_booking'),
    path('view_booking/', views.view_booking, name='view_booking'),
    path('edit/<booking_id>', views.edit_booking, name='edit_booking'),
    path('delete/<booking_id>', views.delete_booking, name='delete_booking'),
    path('today_specials/', views.view_specials, name='today_specials'),
    path('add_specials/', views.add_specials, name='add_specials'),
    path('edit_specials/<special_id>', views.edit_specials, name='edit_specials'),
    path('delete_specials/<special_id>', views.delete_specials, name='delete_specials'),
]
