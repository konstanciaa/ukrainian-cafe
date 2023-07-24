from . import views
from django.urls import path
# from .views import BookingView, SpecialsView
from .views import SpecialsView


urlpatterns = [
    path('', views.SpecialsView.as_view(), name='home'),
    path('add_booking/', views.add_booking, name='add_booking'),
    path('view_booking/', views.view_booking, name='view_booking'),
    path('edit/<booking_id>', views.edit_booking, name='edit_booking'),
]
