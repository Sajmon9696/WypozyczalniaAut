from django.shortcuts import render
from django.views import View
from django.views.generic import ListView, DetailView
from cars.models import Car
from cars.forms import CarFilterForm


# Create your views here.


class ShowCarsView(ListView):
    model = Car
    template_name = "cars/all_cars.html"
    context_object_name = 'cars'


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
            if color:
                cars = cars.filter(car_class=car_class)

        context = {'form': form, 'cars': cars}

        return render(request, self.template_name, context)
