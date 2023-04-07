from django.shortcuts import render
from database.models import Flight
from .forms import SearchFlightForm

def home(request):
    searchFlightForm = SearchFlightForm()

    if request.method == "POST":
        searchFlightForm = SearchFlightForm(request.POST)
        if searchFlightForm.is_valid():
            departure_airport = searchFlightForm.cleaned_data['departure_airport']
            arrival_airport = searchFlightForm.cleaned_data['arrival_airport']
            flights = Flight.objects.all().filter(departure_airport=departure_airport, arrival_airport=arrival_airport)
    else:
        flights = Flight.objects.all()

    context = {
        'searchFlightForm': searchFlightForm,
        "flights": flights,
    }

    return render(request, 'home.html', context)

def reserve(request, flight_id):
    return render(request, 'ticket_reservation.html')

#def home(request):
#    departure_airport = arrival_airport = date = ''
#    if 'departure_airport' in request.POST:
#        departure_airport = request.POST['departure_airport']
#    if 'arrival_airport' in request.POST:
#        arrival_airport = request.POST['arrival_airport']
#    if 'date' in request.POST:
#        date = request.POST['date']
#        
#    print(request.POST)
#    if departure_airport and arrival_airport and date:
#        print(departure_airport)
#        departure_airport_id = Airport.objects.get(slag=departure_airport)
#        arrival_airport_id = Airport.objects.get(slag=arrival_airport)
#        flights = Flight.objects.all().filter(departure_airport=departure_airport_id, arrival_airport=arrival_airport_id, departure_time=date)
#        request.POST = {}
#    else:
#        flights = Flight.objects.all()
#    
#    airports = Airport.objects.all()
#
#    context = {
#        "flights": flights,
#        "airports": airports,
#    }
#    return render(request, "home.html", context)
