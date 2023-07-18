from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

BOOKING_STATUS = ((0, "Booking Confirmed"), (1, "Booking Declined"))
