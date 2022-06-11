from django.contrib import admin
from .models import Station, Booking, ChargerType, Vehicle
# Register your models here.
class StationAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'charger_type', 'price')
    search_fields = ('name', 'address', 'location', 'charger_type')

    class Meta:
        model = Station

class BookingAdmin(admin.ModelAdmin):
    list_display = ('station', 'user', 'date', 'time', 'duration', 'price', 'status')
    search_fields = ('station', 'user', 'date', 'time', 'duration', 'price', 'status')

    class Meta:
        model = Booking

class ChargerTypeAdmin(admin.ModelAdmin):
    list_display = ('id','type')

    class Meta:
        model = ChargerType

class VehicleAdmin(admin.ModelAdmin):
    list_display = ('id','name')

    class Meta:
        model = Vehicle


admin.site.register(Station, StationAdmin)
admin.site.register(Booking, BookingAdmin)
admin.site.register(ChargerType, ChargerTypeAdmin)
admin.site.register(Vehicle, VehicleAdmin)