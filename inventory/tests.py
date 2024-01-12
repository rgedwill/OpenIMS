from django.test import TestCase, Client

# Create your tests here.
from .views import InventoryDeliveryRecord, Inventory
from deliveries.models import Delivery, DeliveryType

class InventoryTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        for deliverytype_id in range(3):
            DeliveryType.objects.create(
                name="deliverytype-0{deliverytype_id}0",
                recurrences="RRULE:FREQ=DAILY",
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
                delivery_type_id= 1,
                unit_delivery_quantity=8,
                sale_price=1000
            )
            Inventory.objects.create(
                name="item-1{inventory_id}1",
                sku= "12345678",
                brand= "BrandX",
                vendor= "coca-cola",
                delivery_type_id= 2,
                unit_delivery_quantity=8,
                sale_price=1000

            )
            Inventory.objects.create(
                name="item-2{inventory_id}2",
                sku= "12345678",
                brand= "BrandX",
                vendor= "coca-cola",
                delivery_type_id= 2,
                unit_delivery_quantity=8,
                sale_price=1000


            )
            
    def test_post(self):
        c = Client()
        
        # using self.captureOnCommitCallbacks is probably useless in this case
        # but it may become useful since it captures callbacks used in the on_commit
        # function that we may or may not use to notify outside systems of creation.
        # https://adamj.eu/tech/2020/05/20/the-fast-way-to-test-django-transaction-on-commit-callbacks/
        with self.captureOnCommitCallbacks(execute=True) as callbacks:
            response = c.post(
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
        # i = Inventory.objects.get(sku=12345671)
        # self.assertEqual(i.sku, 12345678)
        print(callbacks)
        self.assertEqual(response.status_code, 201)
            

        


# This test assumes you've generated the official development dataset
# class InventoryDeliveryRecordTestCase(TestCase):
#     @classmethod
#     def setUpTestData(cls):
#         for deliverytype_id in range(3):
#             DeliveryType.objects.create(
#                 name="deliverytype-0{deliverytype_id}0",
#                 recurrences="RRULE:FREQ=DAILYEXRULE:FREQ=WEEKLY;BYDAY=MO",
#                 start_date="2023-12-17",
#                 next_delivery_date="2025-12-19 09:09:09"
#             )
#             DeliveryType.objects.create(
#                 name="deliverytype-1{deliverytype_id}1", 
#                 recurrences="RRULE:FREQ=WEEKLY;BYDAY=TH,SA",
#                 start_date="2023-12-17",
#                 next_delivery_date="2025-12-19 09:09:09"
#             )
#             DeliveryType.objects.create(
#                 name="deliverytype-1{deliverytype_id}1",
#                 recurrences="RRULE:FREQ=WEEKLY;BYDAY=TU,TH",
#                 start_date="2023-12-17",
#                 next_delivery_date="2025-12-19 09:09:09"
#             )


#         for inventory_id in range(12):
#             Inventory.objects.create(
#                 name="item-0{inventory_id}0",
#                 sku= "12345678",
#                 brand= "BrandX",
#                 vendor= "coca-cola",
#                 delivery_type= "default",
#             )
#             Inventory.objects.create(
#                 name="item-1{inventory_id}1",
#                 sku= "12345678",
#                 brand= "BrandX",
#                 vendor= "coca-cola",
#                 delivery_type= "cold-chain",
#             )
#             Inventory.objects.create(
#                 name="item-2{inventory_id}2",
#                 sku= "12345678",
#                 brand= "BrandX",
#                 vendor= "coca-cola",
#                 delivery_type= "cold-chain",
#             )
#     #checks to ensure
#     # 1. next delivery date is correct
#     # 2. new inventorydeliveryrecord is created
#     # def test_perform_create(self):
#     #     num_inventory=12
#     #     num_delivery_types=3
#     #     num_deliveries=2
#     #     c = Client()
#     #     response = c.post(
#     #         '/inventory-delivery-record/',
#     #         {
#     #             "delivery"
#     #         }
#     #         )
        

#         # def test_perform_create(self):




