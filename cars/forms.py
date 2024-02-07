from django.forms import ModelForm, Form
from django import forms

from cars.models import Car, CarClass


class CarFilterForm(ModelForm):
    class Meta:
        model = Car
        fields = ['model', 'fuel', 'engine_size', 'color']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['color'].required = False
        self.fields['fuel'].required = False
        self.fields['engine_size'].required = False
        self.fields['model'].required = False
        self.fields['car_class'] = forms.MultipleChoiceField(
            choices=[(price.id, price.car_class_name) for price in CarClass.objects.all()], required=False)



