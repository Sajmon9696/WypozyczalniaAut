from django.urls import path

from reservations.views import ReservationListView, ReservationDetailView, ReservationUpdateView, \
    ReservationDeleteView, CreateReservationView, FinishReservationWithFilters

app_name = 'reservations'

urlpatterns = [
    path('create_reservation/', CreateReservationView.as_view(), name='create_reservation'),
    path('your_reservations/', ReservationListView.as_view(), name='your_reservations'),
    path('your_reservation_detail/<int:pk>', ReservationDetailView.as_view(), name='reservation_detail'),
    path('edit_reservation/<int:pk>', ReservationUpdateView.as_view(), name='edit_reservation'),
    path('delete_reservation/<int:pk>', ReservationDeleteView.as_view(), name='delete_reservation'),
    path('finish_reservation/<int:pk>', FinishReservationWithFilters.as_view(), name='finish_reservation'),
]
