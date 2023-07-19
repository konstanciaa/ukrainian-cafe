from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

BOOKING_STATUS = ((0, "Booking Confirmed"), (1, "Booking Declined"))


class Customer(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30, null=True, blank=True)
    last_name = models.CharField(max_length=50, null=True, blank=True)
    phone = models.CharField(max_length=15, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)

    def __str__(self):
        return self.user.username


class Booking(models.Model):
    first_name = models.CharField(max_length=30, null=False, blank=False)
    last_name = models.CharField(max_length=50, null=False, blank=False)
    phone = models.CharField(max_length=15, null=False, blank=False)
    email = models.EmailField()
    date = models.DateField(null=False, blank=False)
    time = models.CharField(null=False, blank=False, max_length=5)
    guests = models.IntegerField(default=2, blank=False)
    booking_status = models.IntegerField(choices=BOOKING_STATUS, default=0)
    customer = models.ForeignKey(Customer, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.first_name + ' ' + self.last_name + "'s" + ' Booking'


