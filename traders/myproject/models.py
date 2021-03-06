from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

class Car(models.Model):
    brand = models.TextField(blank=False)
    model = models.TextField(blank=False)
    image = models.ImageField(upload_to='images')
    price = models.DecimalField(max_digits=20, decimal_places=2)
    transmission = models.TextField(blank=False)
    mileage = models.IntegerField(blank=False)
    description = models.TextField(blank=False)
    
    def __str__(self):
        return self.brand



class Offer(models.Model):
    model = models.TextField(blank=False)
    name = models.CharField(max_length=70, blank=False)
    email = models.EmailField(max_length=254, blank=False)
    contact_number = PhoneNumberField()
    amount = models.IntegerField(blank=False)
    message = models.TextField(blank=True)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Reservation(models.Model):
    full_name = models.TextField(blank=False)
    email = models.EmailField(max_length=254, blank=False)
    message = models.TextField(blank=False)
    contact_number = PhoneNumberField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name

    

