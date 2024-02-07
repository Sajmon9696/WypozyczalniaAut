from django.forms import ModelForm, Form
from django import forms

from cars.models import Car, CarClass


class CarFilterForm(ModelForm):
    class Meta:
        model = Car
        fields = ['model', 'fuel', 'engine_size', 'color']
        widgets = {
            'color': forms.CheckboxSelectMultiple(),
            'fuel': forms.CheckboxSelectMultiple(),
            'engine_size': forms.CheckboxSelectMultiple(),
            'model': forms.CheckboxSelectMultiple(),
        }
        required = {
            'color': False,
            'fuel': False,
            'engine_size': False,
            'model': False,
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['car_class'] = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,
                                                             choices=[(price.id, price.car_class_name) for price in
                                                                      CarClass.objects.all()], required=False)
