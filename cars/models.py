from django.db import models


# Create your models here.

class Color(models.Model):
    color_name = models.CharField(max_length=64)


class Fuel(models.Model):
    fuel_name = models.CharField(max_length=64)


class EngineSize(models.Model):
    engin_size_name = models.CharField(max_length=64)


class Brand(models.Model):
    brand_name = models.CharField(max_length=64)


class CarClass(models.Model):
    car_class_name = models.CharField(max_length=64)
    price = models.PositiveIntegerField()


class CarModel(models.Model):
    model_name = models.CharField(max_length=64)
    car_class = models.ForeignKey(CarClass, on_delete=models.CASCADE)
    car_brand = models.ForeignKey(Brand, on_delete=models.CASCADE)


class Car(models.Model):
    model = models.ForeignKey(CarModel, on_delete=models.CASCADE)
    fuel = models.ForeignKey(Fuel, on_delete=models.CASCADE)
    engine_size = models.ForeignKey(EngineSize, on_delete=models.CASCADE)
    color = models.ForeignKey(Color, on_delete=models.CASCADE)
