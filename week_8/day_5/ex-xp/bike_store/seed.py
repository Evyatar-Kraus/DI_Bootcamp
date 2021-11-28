import os
# Configure settings for project
# Need to run this before calling models from application!
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bike_store.settings')

import django
# Import settings
django.setup()

import random
from faker import Faker
from rent.models import Customer, RentalRate, Rental, Vehicle,VehicleSize,VehicleType
# import os
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "rent.settings")

# import django
# django.setup()

# from django.core.management import call_command
fake = Faker()

def generate_customer_attrs():
    customer_attrs = {
        'country':fake.country(),
        'city':fake.city(),
        'address':fake.address(),
        'first_name': fake.first_name(),
        'last_name': fake.last_name(),
        'phone_number': fake.phone_number(),
        'email': fake.email()
    }

    return customer_attrs


vehicle_type_list = [
    'car','bike','electric bike', 'motorcycle','helicopter','airplane','yacht','boat','scooter','rv']


generate_vehicle_type =  lambda :  {'name':fake.word(ext_word_list=vehicle_type_list)}

vehicle_size_list = [
    'xs','small','medium','large','xl','2xl']

generate_vehicle_size =  lambda :  {'name':fake.word(ext_word_list=vehicle_size_list)}

generate_rental_rate = lambda : {
    'daily_rate':fake.pydecimal(min_value=0,max_value=1000,right_digits=5),
    'vehicle_type': random.choice(list(VehicleType.objects.all())),
    'vehicle_size': random.choice(list(VehicleSize.objects.all())),
    }


def new_fake_customer():
    new_customer  = Customer(**generate_customer_attrs())
    # print(new_customer)
    new_customer.save()
    # print(Customer.objects.all())
new_fake_customer()

def new_fake_vehicle_type():
    new_vehicle_type  = VehicleType(**generate_vehicle_type())
    # print(new_customer)
    new_vehicle_type.save()
    print(new_vehicle_type)

def new_fake_vehicle_size():
    new_vehicle_size  = VehicleSize(**generate_vehicle_size())
    # print(new_customer)
    new_vehicle_size.save()
    print(new_vehicle_size)

# new_fake_vehicle_type()

# new_fake_vehicle_size()


def new_fake_rental_rate():
    new_rental_rate = RentalRate(**generate_rental_rate())
    print(new_rental_rate.daily_rate)
    new_rental_rate.save()
    print(new_rental_rate)
new_fake_rental_rate()