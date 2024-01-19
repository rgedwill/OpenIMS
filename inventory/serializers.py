from rest_framework import serializers
from inventory.models import Inventory, InventoryDeliveryRecord

class InventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Inventory
        fields = [
            'name', 
            'sku', 
            'brand', 
            'vendor', 
            'delivery_type',
            'unit_delivery_quantity', 
            'sale_price'
        ]

class InventoryDeliveryRecordSerializer(serializers.ModelSerializer):
    # user_created = serializers.ReadOnlyField(source='user_created.id')

        
    class Meta:
        model = InventoryDeliveryRecord
        fields = [
            'inventory',
            'quantity',
            'unit_order_price',
            'user_created',
            'date_created',

        ]