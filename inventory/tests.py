from django.test import TestCase, Client
from rest_framework import status

from rest_framework.test import APITestCase

# Create your tests here.
from .views import InventoryDeliveryRecord, Inventory
from deliveries.models import Delivery, DeliveryType

class InventoryTestCase(APITestCase):
    @classmethod
    def setUpTestData(cls):
        for deliverytype_id in range(3):
            DeliveryType.objects.create(
                name=f"deliverytype-0{deliverytype_id}0",
                recurrences="RRULE:FREQ=DAILY",
                start_date="2023-12-17",
                next_delivery_date="2025-12-19 09:09:09"
            )
            
            DeliveryType.objects.create(
                name=f"deliverytype-1{deliverytype_id}1", 
                recurrences="RRULE:FREQ=WEEKLY;BYDAY=TH,SA",
                start_date="2023-12-17",
                next_delivery_date="2025-12-19 09:09:09"
            )
            
            DeliveryType.objects.create(
                name=f"deliverytype-1{deliverytype_id}1",
                recurrences="RRULE:FREQ=WEEKLY;BYDAY=TU,TH",
                start_date="2023-12-17",
                next_delivery_date="2025-12-19 09:09:09"
            )


        for inventory_id in range(12):
            Inventory.objects.create(
                name=f"item-0{inventory_id}0",
                sku= "12345678",
                brand= "BrandX",
                vendor= "coca-cola",
                delivery_type_id= 1,
                unit_delivery_quantity=8,
                sale_price=1000
            )
            
            Inventory.objects.create(
                name=f"item-1{inventory_id}1",
                sku= "12345678",
                brand= "BrandX",
                vendor= "coca-cola",
                delivery_type_id= 2,
                unit_delivery_quantity=8,
                sale_price=1000
            )
            
            Inventory.objects.create(
                name=f"item-2{inventory_id}2",
                sku= "12345678",
                brand= "BrandX",
                vendor= "coca-cola",
                delivery_type_id= 2,
                unit_delivery_quantity=8,
                sale_price=1000
            )
            
    def test_post(self):
        
        # using self.captureOnCommitCallbacks is probably useless in this case
        # but it may become useful since it captures callbacks used in the on_commit
        # function that we may or may not use to notify outside systems of creation.
        # https://adamj.eu/tech/2020/05/20/the-fast-way-to-test-django-transaction-on-commit-callbacks/
        with self.captureOnCommitCallbacks(execute=True) as callbacks:
            response = self.client.post(
                "/inventory/", 
                {
                    "name": "Premium Laptop",
                    "sku": 12345678,
                    "brand": "BrandX",
                    "vendor": "coca-cola",
                    "unit_delivery_quantity": 8,
                    "sale_price": 1000,
                    "delivery_type_id": 2
                }
            )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
            
    def test_get(self):
        import json
        
        response = self.client.get('/inventory/', format=json)
        response.render()
        json_response_content = json.loads(response.content)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(json_response_content), 36)
        
        
class InventoryDeliveryRecordTestCase(APITestCase):
    @classmethod
    def setUpTestData(cls):
        for deliverytype_id in range(3):
            DeliveryType.objects.create(
                name=f"deliverytype-0{deliverytype_id}0",
                recurrences="RRULE:FREQ=DAILY",
                start_date="2023-12-17",
                next_delivery_date="2025-12-19 09:09:09"
            )
            
            DeliveryType.objects.create(
                name=f"deliverytype-1{deliverytype_id}1", 
                recurrences="RRULE:FREQ=WEEKLY;BYDAY=TH,SA",
                start_date="2023-12-17",
                next_delivery_date="2025-12-19 09:09:09"
            )
            
            DeliveryType.objects.create(
                name=f"deliverytype-1{deliverytype_id}1",
                recurrences="RRULE:FREQ=WEEKLY;BYDAY=TU,TH",
                start_date="2023-12-17",
                next_delivery_date="2025-12-19 09:09:09"
            )

        for inventory_id in range(12):
            Inventory.objects.create(
                name=f"item-0{inventory_id}0",
                sku= "12345678",
                brand= "BrandX",
                vendor= "coca-cola",
                delivery_type_id= 1,
                unit_delivery_quantity=8,
                sale_price=1000
            )
            
            Inventory.objects.create(
                name=f"item-1{inventory_id}1",
                sku= "12345678",
                brand= "BrandX",
                vendor= "coca-cola",
                delivery_type_id= 2,
                unit_delivery_quantity=8,
                sale_price=1000
            )
            
            Inventory.objects.create(
                name=f"item-2{inventory_id}2",
                sku= "12345678",
                brand= "BrandX",
                vendor= "coca-cola",
                delivery_type_id= 2,
                unit_delivery_quantity=8,
                sale_price=1000
            )
            
    #checks to ensure
    # 1. next delivery date is correct
    # 2. new inventorydeliveryrecord is created
    # def test_perform_create(self):
    #     num_inventory=12
    #     num_delivery_types=3
    #     num_deliveries=2
    #     c = Client()
    #     response = c.post(
    #         '/inventory-delivery-record/',
    #         {
    #             "delivery"
    #         }
    #         )
        

        # def test_perform_create(self):




