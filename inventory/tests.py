from django.test import TestCase

# Create your tests here.
from .views import InventoryDeliveryRecord, Inventory
from deliveries.models import Delivery, DeliveryType

# This test assumes you've generated the official development dataset
class InventoryDeliveryRecordTestCase(TestCase):

    #checks to ensure
    # 1. next delivery date is correct
    # 2. new inventorydeliveryrecord is created
    def test_perform_create(self):
        num_inventory=12
        num_delivery_types=3
        num_deliveries=2

        @classmethod
        def setUpTestData(cls):
            for deliverytype_id in range(3):
                DeliveryType.objects.create(
                    name="deliverytype-0{deliverytype_id}0",
                    recurrences="RRULE:FREQ=DAILYEXRULE:FREQ=WEEKLY;BYDAY=MO",
                    start_date="2023-12-17",
                    next_delivery_date="2025-12-19 09:09:09"
                )
                DeliveryType.objects.create(
                    name="deliverytype-1{deliverytype_id}1",
                    recurrences="RRULE:FREQ=WEEKLY;BYDAY=TH,SA",
                    start_date="2023-12-17",
                    next_delivery_date="2025-12-19 09:09:09"
                )
                DeliveryType.objects.create(
                    name="deliverytype-1{deliverytype_id}1",
                    recurrences="RRULE:FREQ=WEEKLY;BYDAY=TU,TH",
                    start_date="2023-12-17",
                    next_delivery_date="2025-12-19 09:09:09"
                )


            for inventory_id in range(12):
                Inventory.objects.create(
                    name="item-0{inventory_id}0",
                    sku= "12345678",
                    brand= "BrandX",
                    vendor= "coca-cola",
                    delivery_type= "default",
                )
                Inventory.objects.create(
                    name="item-1{inventory_id}1",
                    sku= "12345678",
                    brand= "BrandX",
                    vendor= "coca-cola",
                    delivery_type= "cold-chain",
                )
                Inventory.objects.create(
                    name="item-2{inventory_id}2",
                    sku= "12345678",
                    brand= "BrandX",
                    vendor= "coca-cola",
                    delivery_type= "cold-chain",
                )