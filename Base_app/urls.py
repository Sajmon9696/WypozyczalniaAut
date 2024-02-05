from django.urls import path

from Base_app.views import main_view
from cars.views import my_view
from cars.views import ShowCarsView, ShowCarDetailView

app_name = 'Base_app'
urlpatterns = [
    path('', main_view, name='main')
]
