from django.shortcuts import render

from rest_framework import generics
from rest_framework.renderers import TemplateHTMLRenderer
from django.http import Http404
from rest_framework.response import Response
from inventory.models import Inventory, InventoryDeliveryRecord
from inventory.serializers import InventorySerializer, InventoryDeliveryRecordSerializer
from deliveries.models import Delivery, DeliveryType
from datetime import datetime
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
        
        # always use validated_data at this stage, can't remember where I read that lol classic
        inventory_object = serializer.validated_data['inventory']
        
        # handy wee method I found for datetime here to just return the date part of a datetime object
        next_delivery_date = datetime.date(inventory_object.delivery_type.next_delivery_date)
        
        # initialize to fail gracefully
        d = Delivery()
        
        # using try/except instead of if/else due to this answer
        # https://stackoverflow.com/a/1835844/5877575
        # 
        # since an exception will only occur on a single delivery once, it should
        # be faster. This may not matter in any cases except for if/when we add
        # importing functionality through this pipeline.
        try:
            d = Delivery.objects.get(delivery_date=next_delivery_date)
        except Delivery.DoesNotExist as e:
            
            # printing both the error and the creation to easily track this behavior in logs
            print(e)
            print("Creating new delivery record... ")
            d = Delivery(delivery_date=next_delivery_date, delivery_type=inventory_object.delivery_type)
            d.save()
        
        serializer.save()

class InventoryDeliveryRecordDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = InventoryDeliveryRecord.objects.all()
    serializer_class = InventoryDeliveryRecordSerializer