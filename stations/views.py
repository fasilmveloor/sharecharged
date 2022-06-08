from rest_framework.generics import (GenericAPIView, ListAPIView, RetrieveAPIView, ListCreateAPIView)
from .models import Station, Booking, ChargerType
from .serializers import StationSerializer, BookingSerializer, ChargerTypeSerializer
from rest_framework.response import Response

class StationListView(ListCreateAPIView):
    queryset = Station.objects.all()
    serializer_class = StationSerializer

    def list(self, request):
        queryset = self.get_queryset().filter(location = request.GET.get('location'))
        serializer = StationSerializer(queryset, many=True)
        return Response(serializer.data)

class StationDetailView(RetrieveAPIView):
    queryset = Station.objects.all()
    serializer_class = StationSerializer

class BookingListView(ListCreateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

    def list(self, request):
        queryset = self.get_queryset().filter(station = request.GET.get('station'))
        serializer = BookingSerializer(queryset, many=True)
        return Response(serializer.data)

class BookingDetailView(RetrieveAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

class ChargerTypeListView(ListAPIView):
    queryset = ChargerType.objects.all()
    serializer_class = ChargerTypeSerializer