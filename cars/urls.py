from django.urls import path

from cars.views import ShowCarsView, ShowCarDetailView

app_name = 'cars'
urlpatterns = [
    path('cars/', ShowCarsView.as_view(), name='all_cars'),
    path('cars_detail/<int:pk>', ShowCarDetailView.as_view(), name='car_detail'),

]