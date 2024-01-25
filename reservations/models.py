from django.db import models

from cars.models import Car


# Create your models here.


class Reservation(models.Model):
    reservation_start_date = models.DateField()
    reservation_end_date = models.DateField()
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='car_reservation')
    user = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='user_reservation')
