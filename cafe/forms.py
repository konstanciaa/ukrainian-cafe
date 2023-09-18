"""
Form elements that will appear on booking and
specials forms.
Based on the Booking and Specials models.
"""
from datetime import datetime

from django import forms
from tempus_dominus.widgets import DateTimePicker
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from cloudinary.models import CloudinaryField
from .models import Booking, Specials


class BookingForm(forms.ModelForm):
    """
    Class to create booking form for booking model
    """
    class Meta:
        model = Booking
        fields = (
                'first_name', 'last_name', 'phone', 'email',
                'booking_date', 'time', 'guests'
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.add_input(Submit('submit', 'Submit'))

    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=50)
    phone = forms.CharField(max_length=15)
    email = forms.EmailField(required=True)
    booking_date = forms.DateField(widget=forms.DateInput(
                        attrs={'type': 'date', 'min': datetime.now().date()})
                        )
    time = forms.TimeField(widget=forms.TimeInput(attrs={'type': 'time'}))
    guests = forms.IntegerField()


class SpecialsForm(forms.ModelForm):
    """
    Class to create today's specials form for specials model
    """
    class Meta:
        model = Specials
        fields = ('title', 'description', 'image', 'today')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.add_input(Submit('submit', 'Submit'))

    title = forms.CharField(max_length=50)
    description = forms.CharField(max_length=200)
    image = forms.ImageField()
    today = forms.CharField(required=False, max_length=5)
