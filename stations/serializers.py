from rest_framework import serializers
from stations.models import Station, Booking, ChargerType, Vehicle

class StationSerializer(serializers.ModelSerializer):

    def save(self, **kwargs):
        user = self.context['request'].user
        name = self.validated_data['name']
        location = self.validated_data['location']
        address = self.validated_data['address']
        phone_no = self.validated_data['phone_no']
        zipcode = self.validated_data['zipcode']
        domestic = self.validated_data['domestic']
        kilowatt = self.validated_data['kilowatt']
        charger_type = self.validated_data['charger_type']
        price = self.validated_data['price']
        station = Station.objects.create(user=user, name=name, location=location, address=address, phone_no=phone_no, zipcode=zipcode, domestic=domestic, kilowatt=kilowatt, charger_type=charger_type, price=price)
        station.save()
        return station


    class Meta:
        model = Station
        fields = "__all__"
        
class BookingSerializer(serializers.ModelSerializer):

    def save(self, **kwargs):
        station = Station.objects.get(id=self.validated_data['station'])
        user = self.context['request'].user
        duration = self.validated_data['duration']
        price = station.price * duration
        charger_Type = ChargerType.objects.get(id=self.validated_data['charger_type'])
        vehicle = Vehicle.objects.get(id=self.validated_data['vehicle'])
        date = self.validated_data['date']
        time = self.validated_data['time']
        status = self.validated_data['status']
        booking = Booking.objects.create(station=station, user=user, duration=duration, price=price, charger_type=charger_Type, vehicle=vehicle, date=date, time=time, status=status)
        booking.save()
        return booking

    class Meta:
        model = Booking
        fields = "__all__"

class ChargerTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = ChargerType
        fields = '__all__'

class VehicleSerializer(serializers.ModelSerializer):
    
        class Meta:
            model = Vehicle
            fields = '__all__'