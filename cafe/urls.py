from . import views
from django.urls import path
from .views import BookingView, SpecialsView


urlpatterns = [
    path('', views.SpecialsView.as_view(), name='home'),
    path('booking/', views.BookingView.as_view(), name='booking')
]
