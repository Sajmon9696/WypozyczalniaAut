from django.contrib.auth import login
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

from accounts.forms import MyLoginForm, MySignUpForm


# Create your views here.


class MyLoginView(LoginView):
    form_class = MyLoginForm
    template_name = 'registration/login.html'
    success_url = reverse_lazy('cars:all_cars')

class MySignUpView(CreateView):
    model = User
    form_class = MySignUpForm
    template_name = 'registration/sing_up.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('cars:all_cars')


