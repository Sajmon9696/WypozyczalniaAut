from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.utils import timezone
from django.utils.decorators import method_decorator
from django.views import View
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView

from cars.forms import CarFilterForm
from cars.models import Car, CarClass
from reservations.forms import CreateReservationForm

from reservations.models import Reservation


def user_is_reservation_owner(function):
    def wrap(request, *args, **kwargs):
        reservation = Reservation.objects.get(pk=kwargs['pk'])
        if reservation.user == request.user:
            return function(request, *args, **kwargs)
        else:
            raise Http404("Brak dostępu do rezerwacji")

    return wrap


# Create your views here.
@method_decorator(login_required, name='dispatch')
class CreateReservationView(CreateView):
    model = Reservation
    form_class = CreateReservationForm
    template_name = 'reservations/create_reservation_form.html'
    context_object_name = 'form'

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = request.user
            reservation = form.save(commit=False)
            if reservation.reservation_start_date < timezone.now().date() or \
                    reservation.reservation_end_date < timezone.now().date() or \
                    reservation.reservation_start_date > reservation.reservation_end_date:
                error = "Podana Data Jest nieprawidlowa"
                return render(request, self.template_name, {'form': form, 'error': error})
            reservation.user = user
            reservation.save()
            return redirect('reservations:finish_reservation', reservation.id)
        return render(request, self.template_name, {'form': form})


@method_decorator(login_required, name='dispatch')
class ReservationListView(ListView):
    model = Reservation
    template_name = 'reservations/all_reservations.html'
    context_object_name = 'reservations'

    def get(self, request, *args, **kwargs):
        reservations = Reservation.objects.filter(user=request.user)
        context = {'reservations': reservations}
        return render(request, self.template_name, context)


@method_decorator(login_required, name='dispatch')
@method_decorator(user_is_reservation_owner, name='dispatch')
class ReservationDetailView(DetailView):
    model = Reservation
    template_name = 'reservations/reservations_detail.html'
    context_object_name = 'reservation'


@method_decorator(login_required, name='dispatch')
@method_decorator(user_is_reservation_owner, name='dispatch')
class ReservationUpdateView(UpdateView):
    model = Reservation
    form_class = CreateReservationForm
    template_name = 'reservations/create_reservation_form.html'
    context_object_name = 'form'

    def post(self, request, *args, **kwargs):
        instance = self.get_object()

        form = self.form_class(request.POST, instance=instance)
        if form.is_valid():
            reservation = form.save(commit=False)
            reservation.car = None
            if reservation.reservation_start_date < timezone.now().date() or \
                    reservation.reservation_end_date < timezone.now().date() or \
                    reservation.reservation_start_date > reservation.reservation_end_date:
                error = "Podana Data Jest nieprawidlowa"
                return render(request, self.template_name, {'form': form, 'error': error})
            reservation.save()
            return redirect('reservations:finish_reservation', pk=reservation.id)
        return render(request, self.template_name, {'form': form})


@method_decorator(login_required, name='dispatch')
@method_decorator(user_is_reservation_owner, name='dispatch')
class ReservationDeleteView(DeleteView):
    model = Reservation
    template_name = 'reservations/delete_reservation_form.html'
    context_object_name = 'reservation'
    success_url = reverse_lazy('reservations:your_reservations')


@method_decorator(login_required, name='dispatch')
@method_decorator(user_is_reservation_owner, name='dispatch')
class FinishReservationWithFilters(UpdateView):
    model = Reservation
    template_name = 'reservations/finish_reservation.html'

    def get(self, request, *args, **kwargs):
        reservation = self.get_object()
        reservation_start_date = reservation.reservation_start_date
        reservation_end_date = reservation.reservation_end_date

        available_cars = Car.objects.exclude(
            car_reservation__reservation_start_date__lte=reservation_end_date,
            car_reservation__reservation_end_date__gte=reservation_start_date)
        form = CarFilterForm(request.GET)

        if form.is_valid():
            model = form.cleaned_data.get('model')
            if model:
                available_cars = available_cars.filter(model=model)

            fuel = form.cleaned_data.get('fuel')
            if fuel:
                available_cars = available_cars.filter(fuel=fuel)

            engine_size = form.cleaned_data.get('engine_size')
            if engine_size:
                available_cars = available_cars.filter(engine_size=engine_size)

            color = form.cleaned_data.get('color')
            if color:
                available_cars = available_cars.filter(color=color)

            car_class = form.cleaned_data.get('car_class')
            if car_class:
                available_cars = available_cars.filter(model__car_class__in=car_class)
        car_classes = CarClass.objects.filter(
            id__in=available_cars.values_list('model__car_class', flat=True)).distinct()

        context = {'reservation': reservation, 'available_cars': available_cars, 'car_classes': car_classes,
                   'form': form}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        reservation = self.get_object()
        selected_car_id = request.POST.get('selected_car')
        if selected_car_id:
            selected_car = Car.objects.get(id=selected_car_id)
            reservation.car = selected_car
            reservation.save()
            return redirect('reservations:your_reservations')
        else:
            reservation.delete()
            return redirect('reservations:your_reservations')
