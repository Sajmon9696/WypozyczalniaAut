from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from django import forms


class MyLoginForm(AuthenticationForm):
    username = forms.CharField()
    password = forms.CharField()


class MySignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

