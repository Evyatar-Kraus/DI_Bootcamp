from django.db import models

# Create your models here.

class Person():
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone_number = model
