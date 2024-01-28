from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView

from cars.models import Car
from reservations.forms import CreateReservationForm
from reservations.models import Reservation


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
            reservation.user = user
            reservation.save()
            return redirect('reservations:continue_reservation', reservation.id)
        return render(request, self.template_name, {'form': form})


class ContinueReservation(UpdateView):
    model = Reservation
    template_name = 'reservations/continue_reservation.html'
    fields = ['car']

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        reservation = self.get_object()
        reservation_start_date = reservation.reservation_start_date
        reservation_end_date = reservation.reservation_end_date

        available_cars = Car.objects.all()

        form.fields['car'].queryset = available_cars.exclude(
            car_reservation__reservation_start_date__lte=reservation_end_date,
            car_reservation__reservation_end_date__gte=reservation_start_date)
        return form


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
class ReservationDetailView(DetailView):
    model = Reservation
    template_name = 'reservations/reservations_detail.html'
    context_object_name = 'reservation'


@method_decorator(login_required, name='dispatch')
class ReservationUpdateView(UpdateView):
    model = Reservation
    template_name = 'reservations/create_reservation_form.html'
    context_object_name = 'form'
    fields = ['reservation_start_date', 'reservation_end_date', 'car']


@method_decorator(login_required, name='dispatch')
class ReservationDeleteView(DeleteView):
    model = Reservation
    template_name = 'reservations/delete_reservation_form.html'
    context_object_name = 'reservation'
    success_url = reverse_lazy('reservations:your_reservations')
