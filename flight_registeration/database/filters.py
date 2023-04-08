import django_filters
from .models import Flight

class FlightFilter(django_filters.FilterSet):
    departure_airport_info_name = django_filters.CharFilter(field_name='departure_airport__name', lookup_expr='icontains')
    arrival_airport_info_name = django_filters.CharFilter(field_name='arrival_airport__name', lookup_expr='icontains')
    class Meta:
        model=Flight
        fields= ['departure_time']