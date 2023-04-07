# Generated by Django 4.1.6 on 2023-04-07 21:26

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Airline',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('contact_information', models.TextField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Airport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('location', models.TextField(max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Flight',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('flight_number', models.CharField(max_length=20)),
                ('departure_time', models.DateTimeField(verbose_name='Departure Time')),
                ('arrival_time', models.DateTimeField(verbose_name='Arrival Time')),
                ('airline_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.airline')),
                ('arrival_airport', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Arrival Airport+', to='database.airport')),
                ('departure_airport', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Departure Airport+', to='database.airport')),
            ],
        ),
        migrations.CreateModel(
            name='Passenger',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50, verbose_name='First Name')),
                ('last_name', models.CharField(max_length=50, verbose_name='Last Name')),
                ('contact_information', models.TextField(max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seat_number', models.CharField(max_length=10, null=True, verbose_name='Seat Number')),
                ('ticket_price', models.DecimalField(decimal_places=3, max_digits=10, verbose_name='Ticket Price')),
                ('reservation_date', models.DateTimeField(default=datetime.datetime(2023, 4, 7, 23, 26, 7, 925), verbose_name='Reservation Date')),
                ('flight_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.flight')),
                ('passenger_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.passenger')),
            ],
        ),
    ]