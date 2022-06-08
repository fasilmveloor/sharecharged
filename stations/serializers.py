from rest_framework import serializers
from stations.models import Station, Booking, ChargerType

class StationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Station
        fields = ('id', 'name', 'address', 'location', 'charger_type', 'price')
        
class BookingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Booking
        fields = ('id', 'station', 'user', 'date', 'time', 'duration', 'price', 'status')

class ChargerTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = ChargerType
        fields = ('id', 'type')