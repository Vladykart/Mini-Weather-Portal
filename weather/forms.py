from django.forms import ModelForm, Select
from .models import City


class CityForm(ModelForm):
    class Meta:
        model = City
        fields = ['name']
        widgets = {'name': Select(attrs={
            'class': 'input',
            'id': 'city',
            'required': True,
            'placeholder': 'Search',
        })}
