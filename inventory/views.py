from django.shortcuts import render

from rest_framework import generics
from rest_framework.renderers import TemplateHTMLRenderer
from django.http import Http404
from rest_framework.response import Response
from inventory.models import Inventory, InventoryDeliveryRecord
from inventory.serializers import InventorySerializer, InventoryDeliveryRecordSerializer
from deliveries.models import Delivery, DeliveryType

class InventoryList(generics.ListCreateAPIView):
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer

class InventoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer

class InventoryDeliveryRecordList(generics.ListCreateAPIView):
    queryset = InventoryDeliveryRecord.objects.all()
    serializer_class = InventoryDeliveryRecordSerializer

    def perform_create(self, serializer):
        # write delivery algorithm here
        serializer.save()

class InventoryDeliveryRecordDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = InventoryDeliveryRecord.objects.all()
    serializer_class = InventoryDeliveryRecordSerializer