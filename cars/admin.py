from django.contrib import admin
from cars.models import Fuel, Color, Brand, CarClass, EngineSize, CarModel, Car

# Register your models here.

admin.site.register(Fuel)
admin.site.register(Color)
admin.site.register(Brand)
admin.site.register(CarClass)
admin.site.register(EngineSize)
admin.site.register(CarModel)
admin.site.register(Car)