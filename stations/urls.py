from django.urls import path
from .views import StationListView, StationDetailView, BookingListView, BookingDetailView, ChargerTypeListView, VehicleListView, BookingListViewTest

urlpatterns = [
    path('stations/', StationListView.as_view(), name='station_list'),
    path('station/<int:pk>/', StationDetailView.as_view(), name='station_detail'),
    path('bookings/', BookingListView.as_view(), name='booking_list'),
    path('booking/<int:pk>/', BookingDetailView.as_view(), name='booking_detail'),
    path('mybookings/', BookingListViewTest.as_view(), name='my_bookings'),
    path('charger_types/', ChargerTypeListView.as_view(), name='charger_type_list'),
    path('vehicles/', VehicleListView.as_view(), name='vehicle_list'),
]
