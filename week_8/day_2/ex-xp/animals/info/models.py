from django.db import models
from django.db.models.fields.related import ForeignKey
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.
class Family(models.Model):
    name = models.CharField(max_length=30, unique = True)

    def __str__(self):
        return f'Family: {self.name}'

    def __repr__(self):
        return f'Family: {self.name}'

class Animal(models.Model):
    name = models.CharField(max_length=30, unique = True)
    #how many legs the animal has
    legs = models.PositiveBigIntegerField(validators = [MaxValueValidator(100)])
    #average weight of an adult animal of this type in kg
    weight = models.DecimalField(max_digits =10, decimal_places = 3, validators = [MinValueValidator(0)])
    #the average height of an adult animal of this type in meters
    height = models.DecimalField(max_digits =10, decimal_places = 3, validators = [MinValueValidator(0)])
    #the maximum speed at which this animal can move km/h
    speed = models.DecimalField(max_digits =10, decimal_places = 3, validators = [MinValueValidator(0)])
    #the family to which this animal belongs. (Must reference the Family model - see below).
    family = models.ForeignKey(Family, on_delete=models.PROTECT)


    def __str__(self):
        return f'Animal: {self.name}'

    def __repr__(self):
        return f'Animal: {self.name}'