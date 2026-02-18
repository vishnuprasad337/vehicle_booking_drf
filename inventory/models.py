from django.db import models

from django.core.validators import RegexValidator
from django.utils import timezone


class Vehicle(models.Model):

    FUEL_CHOICES = [
        ('Petrol', 'Petrol'),
        ('Diesel', 'Diesel'),
        ('Electric', 'Electric'),
        ('Hybrid', 'Hybrid'),
    ]

    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    year = models.IntegerField()
    price_per_day = models.DecimalField(max_digits=10, decimal_places=2)
    fuel_type = models.CharField(max_length=20, choices=FUEL_CHOICES)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.brand} {self.name}"


class Booking(models.Model):

    phone_validator = RegexValidator(
        regex=r'^\d{10}$',
        message="Phone number must be 10 digits."
    )

    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    customer_name = models.CharField(max_length=100)
    customer_phone = models.CharField(max_length=10, validators=[phone_validator])
    start_date = models.DateField()
    end_date = models.DateField()
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True)

    def __str__(self):
        return f"{self.customer_name} - {self.vehicle}"

