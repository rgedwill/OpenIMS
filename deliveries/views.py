from django.shortcuts import render
from rest_framework import generics

from deliveries.models import Delivery
from deliveries.serializers import DeliverySerializer
# Create your views here.
class DeliveryList(generics.ListAPIView):
    queryset = Delivery.objects.all()
    serializer_class = DeliverySerializer

class DeliveryDetail(generics.RetrieveAPIView):
    queryset = Delivery.objects.all()
    serializer_class = DeliverySerializer