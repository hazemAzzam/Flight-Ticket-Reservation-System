from rest_framework import serializers
from .models import *

class AirlineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Airline
        fields = "__all__"

class AirportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Airport
        fields = "__all__"

class FlightSerializer(serializers.ModelSerializer):
    departure_airport_info = AirportSerializer(source='departure_airport', read_only=True)
    departure_airport = serializers.PrimaryKeyRelatedField(
        queryset=Airport.objects.all(),
        write_only=True,
        required=True
    )

    arrival_airport_info = AirportSerializer(source='arrival_airport', read_only=True)
    arrival_airport = serializers.PrimaryKeyRelatedField(
        queryset=Airport.objects.all(),
        write_only=True,
        required=True
    )

    airline_info = AirlineSerializer(source='airline_id', read_only=True)
    airline_id = serializers.PrimaryKeyRelatedField(
        queryset=Airline.objects.all(),
        write_only=True,
        required=True
    )
    class Meta:
        model = Flight
        fields = ['id' ,'flight_number', 'departure_airport', 'departure_airport_info', 'arrival_airport', 'arrival_airport_info', 'departure_time', 'arrival_time', 'airline_id', 'airline_info', 'ticket_price']

class PassengerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Passenger
        fields = "__all__"

class ReservationSerializer(serializers.ModelSerializer):
    flight_info = FlightSerializer(source='flight_id', read_only=True)
    flight_id = serializers.PrimaryKeyRelatedField(
        queryset=Flight.objects.all(), 
        write_only=True, 
        required=True
        )

    passenger_info = PassengerSerializer(source='passenger_id', read_only=True)
    passenger_id = serializers.PrimaryKeyRelatedField(
        queryset=Passenger.objects.all(),
        write_only=True,
        required=True
        )
    
    class Meta:
        model = Reservation
        fields = ["id", "flight_info","flight_id", "passenger_info", "passenger_id", "seat_number", "reservation_date"]
    
    #def create(self, validated_data):
    #    idd = validated_data['flight_id']
    #    print(idd)
    #    return super().create(validated_data)