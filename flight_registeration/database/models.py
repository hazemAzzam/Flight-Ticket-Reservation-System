from django.db import models
from datetime import datetime
# Create your models here.

class Airline(models.Model):
    name = models.CharField(max_length=100, null=False)
    contact_information = models.TextField(max_length=100, null=True)

    def __str__(self):
        return f"{self.name}"
class Airport(models.Model):
    name = models.CharField(max_length=100, null=False)
    slag = models.CharField(max_length=4, null=False, unique=True)
    location = models.TextField(max_length=255, null=True)

    def __str__(self):
        return f"{self.name}({self.slag}) - {self.location}"
    
class Flight(models.Model):
    flight_number = models.CharField(max_length=20, null=False)
    departure_airport = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="Departure Airport+")
    arrival_airport = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="Arrival Airport+")
    departure_time = models.DateTimeField(verbose_name="Departure Time", null=False)
    arrival_time = models.DateTimeField(verbose_name="Arrival Time", null=False)
    airline_id = models.ForeignKey(Airline, on_delete=models.CASCADE)
    ticket_price = models.DecimalField(verbose_name="Ticket Price", null=False, max_digits=10, decimal_places=3)

    def __str__(self):
        return f"{self.flight_number}: {self.departure_airport} -> {self.arrival_airport}"

class Passenger(models.Model):
    first_name = models.CharField(max_length=50, null=False, verbose_name="First Name")
    last_name = models.CharField(max_length=50, null=False, verbose_name="Last Name")
    contact_information = models.TextField(max_length=255, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
class Reservation(models.Model):
    flight_id = models.ForeignKey(Flight, on_delete=models.CASCADE)
    passenger_id = models.ForeignKey(Passenger, on_delete=models.CASCADE)
    seat_number = models.CharField(max_length=10, null=True, verbose_name="Seat Number")
    reservation_date = models.DateTimeField(verbose_name="Reservation Date", default=datetime.now())
