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
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    address = models.TextField(max_length=500)
    phone_no = models.CharField(max_length=20)
    zipcode = models.CharField(max_length=10, default='')
    domestic = models.BooleanField(default=False)
    kilowatt = models.FloatField(default=0)
    charger_type = models.ForeignKey(ChargerType, on_delete=models.CASCADE, default=None)
    price = models.FloatField()
    
    def __str__(self):
        return self.name

class Vehicle(models.Model):
    id = models.AutoField(primary_key=True, auto_created=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Booking(models.Model):
    id = models.AutoField(primary_key=True, auto_created=True)
    station = models.ForeignKey(Station, on_delete=models.CASCADE, default=None)
    user = models.ForeignKey(EmailUser, on_delete=models.CASCADE, default=None)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE, default=None)
    date = models.DateField()
    time = models.TimeField()
    duration = models.IntegerField()
    charger_type = models.ForeignKey(ChargerType, on_delete=models.CASCADE, default=None)
    price = models.FloatField()
    status = models.CharField(max_length=100)

    def __str__(self):
        return self.user.first_name + ' ' + self.user.last_name 
