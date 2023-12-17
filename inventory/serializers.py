from rest_framework import serializers
from inventory.models import Inventory

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
    