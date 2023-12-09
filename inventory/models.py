from django.db import models
from datetime import datetime
# Create your models here.
from multiselectfield.utils import get_max_length
from multiselectfield import MultiSelectField

from recurrence.fields import RecurrenceField

class Location(models.Model):
    '''
    Model for a location to put items (units) in.
    '''
    is_floor = models.BooleanField(default=True)
    c_area = models.CharField(max_length=3)
    c_aisle = models.IntegerField()
    c_section = models.CharField(max_length=2)
    c_row = models.IntegerField()
    c_column = models.IntegerField()

DELIVERY_TYPE_DAYS_OF_WEEK_CHOICES = (
    ('sunday', 'Sunday'),
    ('monday', 'Monday'),
    ('tuesday', 'Tuesday'),
    ('wednesday', 'Wednesday'),
    ('thursday', 'Thursday'),
    ('friday', 'Friday'),
    ('saturday', 'Saturday')
)

class DeliveryType(models.Model):
    name = models.CharField(max_length=256)
    
    recurrences = RecurrenceField()

    start_date = models.DateField(auto_now_add=True, blank=True)
    next_delivery_date = models.DateTimeField(blank=True, null=True)

    def save(self, *args, **kwargs):
        # save override example https://stackoverflow.com/a/11821832/5877575
        current_recurrences = self.recurrences
        first_delivery = current_recurrences.after(
            datetime(2023, 9, 9, 0, 0, 0)        
        )
        self.next_delivery_date = first_delivery
        super(DeliveryType, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

class InventoryManager(models.Manager):
    ''' 
    Basic manager for custom utilities on the Inventory class
    '''
    
    def get_sale_price_currency(self):
        '''
        converts sales from cents (how it's stored) to USD as a STRING based on the recommendation
        given in this post:
        https://stackoverflow.com/a/50376841/5877575
        '''
        return str(self.sale_price_cents / 100)

class Inventory(models.Model):
    '''
    Model for the "profile" of an item. Shows pricing, clearances, sku/upc, etc.
    '''

    name = models.CharField(max_length=2000)
    sku = models.IntegerField()
    brand = models.CharField(max_length=1000)
    vendor = models.CharField(max_length=1000)
    delivery_type = models.ForeignKey(DeliveryType, null=True, on_delete=models.SET_NULL)
    unit_delivery_quantity = models.IntegerField() # how many units are delivered in a full casepack
    sale_price = models.IntegerField()

    def __str__(self):
        return str(self.name)

class Unit(models.Model):
    '''
    Model for an "instance" of Inventory. It has a simple, loose connection via foreign key, but
    functions completely differnetly from Inventory. These items can be moved, counted, duplicated,
     defected, etc.
    '''
    inventory = models.ForeignKey(Inventory, on_delete=models.PROTECT)
    location = models.ForeignKey(Location, on_delete=models.PROTECT)
    quantity = models.IntegerField() # Quantity stored in respective location

    # in the case that an item has no location. This is created so that in no situation
    # should a unit ever have to be "deleted," even if the location it was in is deleted
    no_location = models.BooleanField(default=False)

class Delivery(models.Model):
    '''
    Delivery Records
    '''
    inventory = models.ManyToManyField(Inventory, through="InventoryDeliveryRecord")
    created_date = models.DateTimeField(auto_now_add=True, blank=True)
    delivery_date = models.DateField()
    
class InventoryDeliveryRecord(models.Model):
    delivery = models.ForeignKey(Delivery, on_delete=models.PROTECT)
    inventory = models.ForeignKey(Inventory, on_delete=models.PROTECT)
    quantity = models.IntegerField()
    unit_order_price = models.IntegerField()
