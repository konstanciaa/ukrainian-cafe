from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator
from django.utils import timezone
import datetime


# class Customer(models.Model):
#     user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
#     first_name = models.CharField(max_length=30, null=True, blank=True)
#     last_name = models.CharField(max_length=50, null=True, blank=True)
#     phone = models.CharField(max_length=15, null=True, blank=True)
#     email = models.EmailField(null=True, blank=True)

#     def __str__(self):
#         return self.user.username


# Today's Specials model
class Specials(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(unique=True, null=True)
    description = models.TextField(max_length=200)
    image = CloudinaryField('image', default='placeholder')
    today = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class Booking(models.Model):
    user = models.ForeignKey(User, null=True, blank=True,
                                on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30, null=True)
    last_name = models.CharField(max_length=50, null=True)
    phone = models.CharField(max_length=15, null=True)
    email = models.EmailField()
    booking_date = models.DateField(null=True, blank=True)

    def validate_date(booking_date):
        if booking_date < datetime.date.today():
            raise ValidationError("Date cannot be in the past")
    booking_date = models.DateField(null=True, blank=True,
                                        validators=[validate_date])
    time = models.CharField(null=True, blank=True, max_length=5)
    guests = models.PositiveIntegerField(null=True,
                                            validators=[MinValueValidator(1)])
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'first_name', 'last_name', 'booking_date', 'time')
        ordering = ["-created_on"]

    def __str__(self):
        return f' User {self.user} has made a booking \
                    for {self.first_name} {self.last_name} \
                    for {self.guests} people \
                    for {self.booking_date} at {self.time}.'
