from .models import Booking
from django import forms
from tempus_dominus.widgets import DateTimePicker
from datetime import datetime
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ('first_name', 'last_name', 'phone', 'email',
                    'booking_date', 'time', 'guests')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.add_input(Submit('submit', 'Submit'))

    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=50)
    phone = forms.CharField(max_length=15)
    email = forms.EmailField(required=True)
    booking_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date',
                            'min': datetime.now().date()}))
    time = forms.CharField(max_length=5)
    guests = forms.IntegerField()

