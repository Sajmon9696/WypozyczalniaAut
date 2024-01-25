from django.forms import ModelForm

from cars.models import Car
from reservations.models import Reservation


class CreateReservationForm(ModelForm):
    class Meta:
        model = Reservation
        fields = ['reservation_start_date', 'reservation_end_date', 'car', 'user']

