# Uncomment the following imports before adding the Model code

from django.db import models
from django.utils.timezone import now
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.

class CarMake(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    country_of_origin = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name


class CarModel(models.Model):
    car_make = models.ForeignKey('CarMake', on_delete=models.CASCADE)  # Many-to-One relationship
    dealer_id = models.IntegerField()  # Refers to dealer in Cloudant database
    name = models.CharField(max_length=100)
    
    CAR_TYPES = [
        ('SEDAN', 'Sedan'),
        ('SUV', 'SUV'),
        ('WAGON', 'Wagon'),
        ('HATCHBACK', 'Hatchback'),
        ('COUPE', 'Coupe'),
        ('CONVERTIBLE', 'Convertible'),
    ]
    type = models.CharField(max_length=15, choices=CAR_TYPES, default='SUV')
    
    year = models.DateField()  # Date field for the year of the car model
    
    fuel_type = models.CharField(max_length=20, blank=True, null=True)  # Optional field for fuel type (e.g., Petrol, Diesel)
    is_electric = models.BooleanField(default=False)  # Optional field to mark if the car model is electric
    
    def __str__(self):
        return f"{self.car_make.name} {self.name} ({self.type}, {self.year.year})"

