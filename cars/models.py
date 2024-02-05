from django.db import models


# Create your models here.

class Color(models.Model):
    color_name = models.CharField(max_length=64)
    def __str__(self): return f"{self.color_name}"

class Fuel(models.Model):
    fuel_name = models.CharField(max_length=64)
    def __str__(self): return f"{self.fuel_name}"

class EngineSize(models.Model):
    engin_size_name = models.CharField(max_length=64)
    def __str__(self): return f"{self.engin_size_name}"


class Brand(models.Model):
    brand_name = models.CharField(max_length=64)
    def __str__(self): return f"{self.brand_name}"


class CarClass(models.Model):
    car_class_name = models.CharField(max_length=64)
    price = models.PositiveIntegerField()
    def __str__(self): return f"{self.car_class_name}"


class CarModel(models.Model):
    model_name = models.CharField(max_length=64)
    car_class = models.ForeignKey(CarClass, on_delete=models.CASCADE)
    car_brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    def __str__(self): return f'{self.car_brand} {self.model_name}'


class Car(models.Model):
    model = models.ForeignKey(CarModel, on_delete=models.CASCADE)
    fuel = models.ForeignKey(Fuel, on_delete=models.CASCADE)
    engine_size = models.ForeignKey(EngineSize, on_delete=models.CASCADE)
    color = models.ForeignKey(Color, on_delete=models.CASCADE)
    pic = models.ImageField(upload_to='img/', null=True, blank=True)
    def __str__(self): return f'{self.model}'