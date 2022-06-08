from django.db import models
from users.models import EmailUser

class ChargerType(models.Model):
    id = models.IntegerField(primary_key=True, auto_created=True, default=0)
    type = models.CharField(max_length=100)

# Create your models here.
class Station(models.Model):
    id = models.AutoField(primary_key=True, auto_created=True)
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    address = models.TextField(max_length=500)
    phone_no = models.CharField(max_length=20)
    charger_type = models.ForeignKey(ChargerType, on_delete=models.CASCADE, default=None)
    price = models.FloatField()
    
    def __str__(self):
        return self.name

class Booking(models.Model):
    id = models.AutoField(primary_key=True, auto_created=True)
    station = models.ForeignKey(Station, on_delete=models.CASCADE, default=None)
    user = models.ForeignKey(EmailUser, on_delete=models.CASCADE, default=None)
    date = models.DateField()
    time = models.TimeField()
    duration = models.IntegerField()
    price = models.FloatField()
    status = models.CharField(max_length=100)
