from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect
from .models import Customer,Rental,RentalRate,Vehicle,VehicleSize,VehicleType
from .forms import RentalForm,VehicleForm,CustomerForm

# Create your views here.
# def homepage(request):
#     return render(request,'homepage.html',context={})


def rental(request,rental_id):
    rental = get_object_or_404(Rental.objects.get(id=rental_id))
    rentals_data = {'rental':rental}
    return render(request,'rental.html', context = rentals_data )


def rentals(request):
    rental_list = get_list_or_404(Rental.objects.all().latest('return_date'))
    rentals_data = {'rentals':rental_list}
    return render(request,'rentals.html', context =  rentals_data )

def rental_new(request):
    if request.method == 'POST':
        form = RentalForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            rental = Rental.objects.create(**form.cleaned_data)
            return redirect('rental_page',rental.id)
    if request.method == 'GET':
        form = RentalForm()
    return render(request,'rental_new.html', {'form':form})

def customer(request,customer_id):
    customer = get_object_or_404(Customer.objects.get(id=customer_id))
    customer_data = {'customer':customer}
    return render(request,'customer.html', context = customer_data )

def customers(request):
    customers_data = {}
    return render(request,'customers.html', context = customers_data )

def customer_new(request):
    new_customer_data = {}
    form = CustomerForm(request.POST)
    if form.is_valid():
        print(form.cleaned_data)
        customer = Customer.objects.create(**form.cleaned_data)
        return redirect('customer_page',customer.id)
    if request.method == 'GET':
        form = CustomerForm()
    return render(request,'customer_new.html', {'form':form})

def vehicle(request,vehicle_id):
    vehicle = get_object_or_404(Vehicle.objects.get(id= vehicle_id))
    vehicle_data = {' vehicle': vehicle}
    return render(request,'vehicle.html', context = vehicle_data )

def vehicles(request):
    vehicle_list = get_list_or_404(Vehicle.objects.all())
    vehicles_data = {'vehicles':vehicle_list}
    return render(request,'vehicles.html', context = vehicles_data )

def vehicle_new(request):
    if request.method == 'POST':
        form = VehicleForm(request.POST)
    if form.is_valid():
        print(form.cleaned_data)
        vehicle = Vehicle.objects.create(**form.cleaned_data)
        return redirect('vehicle_page',vehicle.id)
    if request.method == 'GET':
        form = VehicleForm()
    return render(request,'vehicle_new.html', {'form':form})