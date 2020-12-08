from rest_framework import viewsets
from . import models
from . import serializers


class CarViewset(viewsets.ModelViewSet):
    queryset = models.Car.objects.all()
    serializer_class = serializers.CarSerializer


class UserViewset(viewsets.ModelViewSet):
    queryset = models.User.objects.all()
    serializer_class = serializers.UserSerializer

class OfferViewset(viewsets.ModelViewSet):
    queryset = models.Offer.objects.all()
    serializer_class = serializers.OfferSerializer

class ReservationViewset(viewsets.ModelViewSet):
    queryset = models.Reservation.objects.all()
    serializer_class = serializers.ReservationSerializer
