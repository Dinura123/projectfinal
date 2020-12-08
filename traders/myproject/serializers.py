from rest_framework import serializers
from myproject.models import Car
from myproject.models import User
from myproject.models import Offer
from myproject.models import Reservation

class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model =Car
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model =User
        fields = '__all__'

class OfferSerializer(serializers.ModelSerializer):
    class Meta:
        model =Offer
        fields = '__all__'

class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model =Reservation
        fields = '__all__'