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
    name = serializers.StringRelatedField()
    # user_created = serializers.ReadOnlyField(source='user_created.id')
    
    def validate_quantity(self, qty):
        if qty < 1:
            raise serializers.ValidationError("Quantity too low. Must order at least one full casepack")
        return qty
        
    class Meta:
        model = InventoryDeliveryRecord
        fields = [
            'name',
            'inventory',
            'quantity',
            'unit_order_price',
            'user_created',
            'date_created',

        ]