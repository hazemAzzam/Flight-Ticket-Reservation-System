from django.urls import path, include
from rest_framework import routers
from .views import *
from database.api import *

router = routers.DefaultRouter()
router.register('Airlines', AirlineAPI)
router.register('Airports', AirportAPI)
router.register('Flights', FlightAPI)
router.register("Passengers", PassengerAPI)
router.register("Reservations", ReservationAPI)

urlpatterns = [
    path('', include(router.urls)),
]
