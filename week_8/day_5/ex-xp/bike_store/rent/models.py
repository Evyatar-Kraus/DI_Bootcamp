from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class Customer(models.Model):
    first_name =  models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = PhoneNumberField()
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)

class VehicleType(models.Model):
    name =  models.CharField(max_length=100, unique=True)

class VehicleSize(models.Model):
    name =  models.CharField(max_length=100, unique=True)

class Vehicle(models.Model):
    vehicle_type = models.ForeignKey(VehicleType,on_delete=models.PROTECT)
    date_created = models.DateTimeField(auto_now_add = True)
    real_cost = models.DecimalField(decimal_places=5,max_digits=20)
    size = models.ForeignKey(VehicleSize,on_delete=models.PROTECT)

class Rental(models.Model):
    rental_date = models.DateTimeField(auto_now_add = True)
    return_date = models.DateTimeField()
    customer = models.ForeignKey(Customer,on_delete=models.PROTECT)
    vehicle = models.ForeignKey(Vehicle,on_delete=models.PROTECT)

class RentalRate(models.Model):
    daily_rate  = models.DecimalField(decimal_places=5,max_digits=20)
    vehicle_type = models.ForeignKey(VehicleType,on_delete=models.PROTECT)
    vehicle_size = models.ForeignKey(VehicleSize,on_delete=models.PROTECT)
