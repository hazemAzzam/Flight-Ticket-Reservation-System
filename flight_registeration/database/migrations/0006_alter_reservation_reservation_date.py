# Generated by Django 4.1.6 on 2023-04-08 22:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0005_alter_reservation_reservation_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='reservation_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 4, 9, 0, 11, 38, 162007), verbose_name='Reservation Date'),
        ),
    ]
