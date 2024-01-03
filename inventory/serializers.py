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
    model = InventoryDeliveryRecord
    # user_created = serializers.ReadOnlyField(source='user_created.id')

    fields = [
        'delivery',
        'inventory',
        'user_created',
        'date_created'
    ]