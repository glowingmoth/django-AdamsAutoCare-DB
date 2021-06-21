from  django import forms
from django.forms import ModelForm
from .models import *


class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'

class AddressForm(ModelForm):
    class Meta:
        model = Address
        fields = '__all__'

class CarForm(ModelForm):
    class Meta:
        model = Car
        fields = '__all__'