from django.urls import path
from .views import *

urlpatterns = [
    path('api/vehicles/', VehicleListCreateAPIView.as_view()),
    path('api/vehicles/<int:pk>/', VehicleDetailAPIView.as_view()),

    path('api/bookings/', BookingListCreateAPIView.as_view()),
    path('api/bookings/<int:pk>/', BookingDetailAPIView.as_view()),
]
