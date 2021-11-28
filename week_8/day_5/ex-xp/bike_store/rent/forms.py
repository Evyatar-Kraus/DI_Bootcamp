from django import forms
from .models import Rental,RentalRate,Customer,VehicleType,VehicleSize,Vehicle


class RentalForm(forms.Form):
    class Meta:
        model = Rental
        fields = ['customer','vehicle']
    # title = forms.CharField(max_length=100)
    # uploader_name = forms.CharField(
    #     widget=forms.TextInput(
    #         attrs={
    #             'placeholder': 'Uploader name',
    #         }
    #     )
    # )
    # url = forms.URLField()
    # field_order = ['title', 'uploader_name', 'url']
    # categories = forms.ModelMultipleChoiceField(
    #     queryset=Category.objects.all()
    # )


class CustomerForm(forms.Form):
    class Meta:
        model = Customer
        fields = ['first_name','last_name','email','phone_number','address','city','country']

class VehicleForm(forms.Form):
    class Meta:
        model = Vehicle
        fields = ['vehicle_type','size','real_cost']