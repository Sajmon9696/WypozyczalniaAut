from django.contrib import admin
import models

# Register your models here.

admin.site.register(models.Fuel)
admin.site.register(models.Color)
admin.site.register(models.Brand)
admin.site.register(models.CarClass)
admin.site.register(models.EngineSize)
admin.site.register(models.CarModel)
admin.site.register(models.Car)