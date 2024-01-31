from django.shortcuts import render

from accounts.forms import MyLoginForm
from cars.models import Car
from reservations.forms import CreateReservationForm
from reservations.views import CreateReservationView


# Create your views here.

def main_view(request):
    form = CreateReservationForm
    cars = Car.objects.all()
    login_form = MyLoginForm
    return render(request, 'Base_app/main.html', {'form': form, 'cars': cars, 'login_form': login_form})
