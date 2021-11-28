from django.urls import path
from . import views

urlpatterns = [
    # path('',views.homepage, name='homepage'),
    path('rent/rental',views.rentals, name="rentals_page"),
    path('rent/rental/<int:rental_id>',views.rental, name="rental_page"),
    path('rent/rental/add',views.rental_new,name="new_rental_page"),
    path('rent/customer',views.customers, name="customers_page"),
    path('rent/customer/<int:customer_id>',views.customer, name="customer_page"),
    path('rent/customer/add',views.customer_new,name="new_customer_page"),
    path('rent/vehicle',views.vehicles, name="vehicles_page"),
    path('rent/vehicle/<int:vehicle_id>',views.customer, name="customer_page"),
    path('rent/vehicle/add',views.vehicle_new,name="new_vehicle_page"),
]
