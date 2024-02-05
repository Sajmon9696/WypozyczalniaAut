from django.shortcuts import render

from accounts.forms import MyLoginForm
from cars.models import Car
from reservations.forms import CreateReservationForm
from reservations.views import CreateReservationView


# Create your views here.
import random

def main_view(request):
    form = CreateReservationForm
    cars = Car.objects.all()
    login_form = MyLoginForm
    random_cars = random.sample(list(cars), 3)
    return render(request, 'Base_app/main.html', {'form': form, 'cars': cars, 'login_form': login_form, 'random_cars':random_cars})


