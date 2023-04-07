from django import forms
from database.models import *

class SearchFlightForm(forms.ModelForm):
    class Meta:
        model = Flight
        fields = ['departure_airport', 'arrival_airport']
        #widgets = {
        #    'departure_time': forms.DateTimeInput(attrs={'type': 'datetime-local'})
        #}

class FlightForm(forms.ModelForm):
    class Meta:
        model = Flight
        exclude = ['id']