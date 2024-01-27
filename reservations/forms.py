from django.forms import ModelForm, Form
from django import forms

from cars.models import Car
from reservations.models import Reservation


class CreateReservationForm(ModelForm):
    class Meta:
        model = Reservation
        fields = ['reservation_start_date', 'reservation_end_date']

