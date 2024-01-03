from rest_framework import serializers
from deliveries.models import Delivery

class DeliverySerializer(serializers.ModelSerializer):
    class Meta:
        model = Delivery
        fields = [
            'created_date',
            'delivery_date',
            'delivery_type'
        ]
