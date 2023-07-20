from . import views
from django.urls import path
# from .views import BookingView, SpecialsView
# from .views import SpecialsView


urlpatterns = [
    path('', views.SpecialsView.as_view(), name='home'),
    path('booking/', views.booking, name='booking')
    # path('booking/', views.BookingView.as_view(), name='booking')
]
