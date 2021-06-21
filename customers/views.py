from django.shortcuts import render
from django.http import HttpResponse


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
    return render(request, 'customers/create.html')

def delete(request, id):
    remove_customer = Customer.objects.get(id=id).delete()
    return render(request, 'customers/index.html')
