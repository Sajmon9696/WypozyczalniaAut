from django.shortcuts import render
from django.views import View
from django.views.generic import ListView, DetailView

import cars.models
from cars.models import Car, CarClass
from cars.forms import CarFilterForm

from django.shortcuts import render
from .models import CarModel, Car


# Create your views here.

def my_view(request):
    cars_a = Car.objects.filter(model__car_class_id="A")
    return render(request, 'cars/all_cars.html', {'cars_a': cars_a})


class ShowCarsView(ListView):
    model = Car
    template_name = "cars/all_cars.html"
    context_object_name = 'cars'

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.order_by('model__car_class')
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['car_classes'] = CarClass.objects.all()
        return context


class ShowCarDetailView(DetailView):
    model = Car
    template_name = "cars/car_detail.html"
    context_object_name = 'car'


class CarFilterView(View):
    template_name = 'cars/filter_cars.html'

    def get(self, request):
        form = CarFilterForm(request.GET)
        cars = Car.objects.all()

        if form.is_valid():
            model = form.cleaned_data.get('model')
            if model:
                cars = cars.filter(model=model)

            fuel = form.cleaned_data.get('fuel')
            if fuel:
                cars = cars.filter(fuel=fuel)

            engine_size = form.cleaned_data.get('engine_size')
            if engine_size:
                cars = cars.filter(engine_size=engine_size)

            color = form.cleaned_data.get('color')
            if color:
                cars = cars.filter(color=color)

            car_class = form.cleaned_data.get('car_class')
            if car_class:
                cars = cars.filter(model__car_class=car_class)

        car_classes = CarClass.objects.filter(id__in=cars.values_list('model__car_class', flat=True)).distinct()

        context = {'form': form, 'cars': cars, 'car_classes': car_classes}

        return render(request, self.template_name, context)
