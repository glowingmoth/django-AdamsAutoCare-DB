from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import *


from .models import *

# Create your views here.

def index(request):
    customers = Customer.objects.all()
    return render(request, 'customers/index.html', {"customers": customers})

def detail(request, id):
    customer = Customer.objects.get(id=id)
    # address = Address.objects.get(id=id)
    # car = Car.objects.get(id=id)
    context = {"customer": customer}  # "address": address, "car": car
    return render(request, 'customers/detail.html', context)

def create(request):

    customer_form = CustomerForm
    address_form = AddressForm
    car_form = CarForm

    if request.method == 'POST':
        customer_form = CustomerForm(request.POST)
        if customer_form.is_valid():
            customer_form.save()
            return redirect('/')

    return render(request, 'customers/create.html', { "customer_form": customer_form, "address_form": address_form, "car_form": car_form })

def delete(request, id):
    customer = Customer.objects.get(id=id)
    if request.method == 'POST':
      customer.delete()
      return redirect('/')

    return render(request, 'customers/delete.html', { "customer": customer })
