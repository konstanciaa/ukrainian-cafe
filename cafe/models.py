"""
Models created to represent booking and specials.
Individual fields are booking components.
Contents in field parentheses represent restrictions.
"""
import datetime
from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator
from django.utils import timezone


# Today's Specials model
class Specials(models.Model):
    """
    Class to represent specials model in database and for
    today's specials form. Individual fields are specials components.
    Contents in field parentheses represent restrictions.
    """
    title = models.CharField(max_length=50)
    slug = models.SlugField(unique=True, null=True)
    description = models.TextField(max_length=200)
    image = CloudinaryField('image', default='placeholder')
    today = models.CharField(max_length=5)

    def __str__(self):
        return self.title


# Booking model
class Booking(models.Model):
    """
    Class to represent booking model in database and for
    booking form. Individual fields are booking components.
    Contents in field parentheses represent restrictions.
    """
    user = models.ForeignKey(
        User, null=True, blank=True, on_delete=models.CASCADE
        )
    first_name = models.CharField(max_length=30, null=True)
    last_name = models.CharField(max_length=50, null=True)
    phone = models.CharField(max_length=15, null=True)
    email = models.EmailField()
    booking_date = models.DateField(null=True, blank=True)

    def validate_date(booking_date):
        """
        Validate date so that booking date
        is not in the past.
        """
        if booking_date < datetime.date.today():
            raise ValidationError("Date cannot be in the past")
    booking_date = models.DateField(
        null=True, blank=True, validators=[validate_date]
        )
    time = models.TimeField(null=True, blank=True)
    guests = models.PositiveIntegerField(
        null=True, validators=[MinValueValidator(1)]
        )
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        """
        Class container with metadata
        attached to the model.
        """
        unique_together = (
            'user', 'first_name', 'last_name', 'booking_date', 'time'
            )
        ordering = ["-created_on"]

    def __str__(self):
        """
        Function to return object model
        items as string.
        """
        return f' User {self.user} has made a booking \
                    for {self.first_name} {self.last_name} \
                    for {self.guests} people \
                    for {self.booking_date} at {self.time}.'
