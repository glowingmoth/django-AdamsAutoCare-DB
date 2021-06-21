from django.db import models
# from django.db.models.fields import CharField


# Create your models here.

class Customer(models.Model):
    first_name = models.CharField(max_length=30, blank=False, null=True)
    last_name = models.CharField(max_length=30, blank=False, null=True)
    phone = models.CharField(max_length=10, blank=False, null=True)
    email = models.EmailField(max_length=254, null=True)
    
    def __str__(self):
        return self.first_name +" "+ self.last_name

class Address(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True)
    house_number = models.CharField(max_length=30, blank=True, null=True)
    street = models.CharField(max_length=30, blank=True, null=True)
    suburb = models.CharField(max_length=30, blank=True, null=True)
    city = models.CharField(max_length=30, blank=True, null=True)
    
class Car(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True)    
    make = models.CharField(max_length=30, blank=True, null=True)
    model = models.CharField(max_length=30, blank=True, null=True)
    year = models.CharField(max_length=4, blank=True, null=True)
    rego = models.CharField(max_length=6, blank=True, null=True)

