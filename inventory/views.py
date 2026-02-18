from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Vehicle, Booking
from .serializers import VehicleSerializer, BookingSerializer


class VehicleListCreateAPIView(APIView):

    def get(self, request):
        vehicles = Vehicle.objects.all()

        brand = request.query_params.get('brand')
        fuel_type = request.query_params.get('fuel_type')
        is_available = request.query_params.get('is_available')

        if brand:
            vehicles = vehicles.filter(brand=brand)

        if fuel_type:
            vehicles = vehicles.filter(fuel_type=fuel_type)

        if is_available:
            vehicles = vehicles.filter(
                is_available=is_available.lower() == 'true'
            )

        serializer = VehicleSerializer(vehicles, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = VehicleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class VehicleDetailAPIView(APIView):

    def get_object(self, pk):
        try:
            return Vehicle.objects.get(pk=pk)
        except Vehicle.DoesNotExist:
            return None

    def get(self, request, pk):
        vehicle = self.get_object(pk)
        if not vehicle:
            return Response({"error": "Vehicle not found"}, status=404)
        return Response(VehicleSerializer(vehicle).data)

    def put(self, request, pk):
        vehicle = self.get_object(pk)
        if not vehicle:
            return Response({"error": "Vehicle not found"}, status=404)

        serializer = VehicleSerializer(vehicle, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=400)

    def delete(self, request, pk):
        vehicle = self.get_object(pk)
        if not vehicle:
            return Response({"error": "Vehicle not found"}, status=404)

        vehicle.delete()
        return Response({"message": "Deleted"}, status=204)


class BookingListCreateAPIView(APIView):

    def get(self, request):
        bookings = Booking.objects.all()
        return Response(BookingSerializer(bookings, many=True).data)

    def post(self, request):
        serializer = BookingSerializer(data=request.data)

        if serializer.is_valid():
            vehicle = serializer.validated_data['vehicle']
            start_date = serializer.validated_data['start_date']
            end_date = serializer.validated_data['end_date']


            days = (end_date - start_date).days
            total_amount = days * vehicle.price_per_day
            booking =(serializer.save(total_amount=total_amount))

            vehicle.is_available = False
            vehicle.save()

            return Response(BookingSerializer(booking).data, status=201)

        return Response(serializer.errors, status=400)


class BookingDetailAPIView(APIView):

    def get_object(self, pk):
        try:
            return Booking.objects.get(pk=pk)
        except Booking.DoesNotExist:
            return None

    def get(self, request, pk):
        booking = self.get_object(pk)
        if not booking:
            return Response({"error": "Booking not found"}, status=404)

        return Response(BookingSerializer(booking).data)

