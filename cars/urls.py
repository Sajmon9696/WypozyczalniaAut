from django.urls import path

from cars.views import ShowCarsView, ShowCarDetailView, CarFilterView

app_name = 'cars'
urlpatterns = [
    path('cars/', ShowCarsView.as_view(), name='all_cars'),
    path('cars/filter', CarFilterView.as_view(), name='filter_cars'),
    path('cars_detail/<int:pk>', ShowCarDetailView.as_view(), name='car_detail'),

]