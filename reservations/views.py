from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView

from reservations.forms import CreateReservationForm
from reservations.models import Reservation


# Create your views here.

@method_decorator(login_required, name='dispatch')
class CreateReservationView(CreateView):
    model = Reservation
    form_class = CreateReservationForm
    template_name = 'reservations/create_reservation_form.html'
    success_url = reverse_lazy('reservations:your_reservations')


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
