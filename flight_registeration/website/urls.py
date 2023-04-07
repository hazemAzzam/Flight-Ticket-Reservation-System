from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('<int:flight_id>/reserve/', reserve, name='reserve')
]