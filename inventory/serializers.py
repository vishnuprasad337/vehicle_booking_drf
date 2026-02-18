from rest_framework import serializers
from .models import Vehicle, Booking
from django.utils import timezone


class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = '__all__'


class BookingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Booking
        fields = '__all__'
        read_only_fields = ['total_amount']

    def validate(self, data):
        vehicle = data['vehicle'] 

        if not vehicle.is_available:
            raise serializers.ValidationError("Vehicle is not available.")

        if data['start_date'] < timezone.now().date():
            raise serializers.ValidationError("Start date cannot be in the past.")

        if data['end_date'] <= data['start_date']:
            raise serializers.ValidationError("End date must be after start date.")

        overlapping = Booking.objects.filter(
            vehicle=data['vehicle'],
            start_date__lt=data['end_date'],
            end_date__gt=data['start_date']
        ).exists()

        if overlapping:
            raise serializers.ValidationError("Vehicle already booked for these dates.")

        return data
