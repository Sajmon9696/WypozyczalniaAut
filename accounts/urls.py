from django.urls import path
from accounts.views import MyLoginView, MySignUpView
from django.contrib.auth import views as auth_views

app_name = 'accounts'

urlpatterns = [
    path('login/', MyLoginView.as_view(), name='login'),
    path('registration/', MySignUpView.as_view(), name='register_user'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]