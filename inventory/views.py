from django.http import Http404
from django.db.models import Sum

from rest_framework import generics

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
        '''
        Overrides the perform_create method in the drf CreateModelMixin (mixins.py).
        As seen in the source code, the only line required to be called to keep functionality the same
        is serializer.save(). The rest of drf's logic occurs in create() which calles perform_create(),
        so this is basically like a super().

        Most of the logic is tied to checking if a delivery record already exists, and creating/updating
        the Delivery or InventoryDeliveryRecord as necessary.
        asd'''
        # always use validated_data at this stage, can't remember where I read that lol classic
        inventory_object = serializer.validated_data['inventory']

        delivery_type_object = inventory_object.delivery_type
        if delivery_type_object is None:
            
            # This value error is most often caused by an API user inputting an invalid inventory_id
            raise ValueError("Related delivery type does not exist")

        # handy wee method I found for datetime here to just return the date part of a datetime object
        next_delivery_date = datetime.date(delivery_type_object.next_delivery_date)
        
        # if next_delivery_date is before right now, recalculate the next recurrence
        if next_delivery_date < datetime.date(datetime.now()):
            next_delivery_date = delivery_type_object.recurrences.after(datetime.now())
        
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
            
        print(d.id)
        serializer.validated_data['delivery_id'] = d.id
        serializer.save()

    def get_queryset(self):
        
        # returns annotated table with the sum of quantities for each inventory item
        return InventoryDeliveryRecord.objects.annotate(Sum("quantity"))
    
class InventoryDeliveryRecordDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = InventoryDeliveryRecord.objects.all()
    serializer_class = InventoryDeliveryRecordSerializer