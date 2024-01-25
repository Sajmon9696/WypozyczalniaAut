from django.shortcuts import render
from django.views.generic import ListView, DetailView
from cars.models import Car

# Create your views here.


class ShowCarsView(ListView):
    model = Car
    template_name = "cars/all_cars.html"
    context_object_name = 'cars'


class ShowCarDetailView(DetailView):
    model = Car
    template_name = "cars/car_detail.html"
    context_object_name = 'car'

