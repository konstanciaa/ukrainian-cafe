from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator
from django.utils import timezone

# BOOKING_STATUS = ((0, "Awaiting Confirmation"), (1, "Booking Confirmed"), (2, "Booking Declined"))


# class Customer(models.Model):
#     user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
#     first_name = models.CharField(max_length=30, null=True, blank=True)
#     last_name = models.CharField(max_length=50, null=True, blank=True)
#     phone = models.CharField(max_length=15, null=True, blank=True)
#     email = models.EmailField(null=True, blank=True)

#     def __str__(self):
#         return self.user.username


# # Booking model for making a reservation 
# class Booking(models.Model):
#     first_name = models.CharField(max_length=30, null=False, blank=False)
#     last_name = models.CharField(max_length=50, null=False, blank=False)
#     phone = models.CharField(max_length=15, null=False, blank=False)
#     email = models.EmailField()
#     date = models.DateField(null=False, blank=False)
#     time = models.CharField(null=False, blank=False, max_length=5)
#     guests = models.IntegerField(default=2, blank=False)
#     booking_status = models.IntegerField(choices=BOOKING_STATUS, default=0)
#     confirmed = models.BooleanField(default=False)
#     customer = models.ForeignKey(Customer, null=True, on_delete=models.CASCADE)

#     def __str__(self):
#         return self.first_name + ' ' + self.last_name + "'s" + ' Booking'


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
    first_name = models.CharField(max_length=30, null=True, blank=True)
    last_name = models.CharField(max_length=50, null=True, blank=True)
    phone = models.CharField(max_length=15, null=True, blank=True)
    email = models.EmailField()
    date_time = models.DateTimeField(null=True)

    def validate_date(date_time):
        if date_time < timezone.now():
            raise ValidationError("Date cannot be in the past")
    date_time = models.DateTimeField(null=True, blank=True,
                                        validators=[validate_date])
    guests = models.PositiveIntegerField(null=True,
                                            validators=[MinValueValidator(1)])
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'first_name', 'last_name', 'date_time')
        ordering = ["-created_on"]

    def __str__(self):
        return f' User {self.user} has made a booking \
                    for {self.first_name} {self.last_name} \
                    for {self.guests} people \
                    for {self.date_time}.'
