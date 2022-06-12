from django.db import models
from users.models import EmailUser

class ChargerType(models.Model):
    id = models.IntegerField(primary_key=True, auto_created=True, default=0)
    type = models.CharField(max_length=100)

    def __str__(self):
        return self.type

# Create your models here.
class Station(models.Model):
    id = models.AutoField(primary_key=True, auto_created=True)
    user = models.ForeignKey(EmailUser, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    location = models.CharField(max_length=100, null=True, blank=True)
    address = models.TextField(max_length=500, null=True, blank=True)
    phone_no = models.CharField(max_length=20, null=True, blank=True)
    zipcode = models.CharField(max_length=10, default='', null=True, blank=True)
    domestic = models.BooleanField(default=False, null=True, blank=True)
    kilowatt = models.FloatField(default=0, null=True, blank=True)
    charger_type = models.ForeignKey(ChargerType, on_delete=models.CASCADE, default=None, null=True, blank=True)
    price = models.FloatField(null=True, blank=True)
    
    def __str__(self):
        return self.name

class Vehicle(models.Model):
    id = models.AutoField(primary_key=True, auto_created=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Booking(models.Model):
    id = models.CharField(primary_key=True, max_length=100, auto_created=True)
    station = models.ForeignKey(Station, on_delete=models.CASCADE, default=None)
    user = models.ForeignKey(EmailUser, on_delete=models.CASCADE, default=None)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE, default=None)
    date = models.DateField()
    time = models.TimeField()
    phone_no = models.CharField(max_length=20, null=True, blank=True)
    charger_type = models.ForeignKey(ChargerType, on_delete=models.CASCADE, default=None)
    

    def __str__(self) -> str:
        print(type(self))
        return self.id
