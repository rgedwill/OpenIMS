from django.conf import settings
from django.db import models
from datetime import datetime
# Create your models here.

from recurrence.fields import RecurrenceField
from deliveries.models import DeliveryType, Delivery
from accounts.models import CustomUser


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
    sku = models.CharField(max_length=10)
    brand = models.CharField(max_length=1000)
    vendor = models.CharField(max_length=1000)
    delivery_type = models.ForeignKey(DeliveryType, null=True, on_delete=models.SET_NULL)
    unit_delivery_quantity = models.IntegerField() # how many units are delivered in a full casepack
    sale_price = models.IntegerField()

    class Meta:
        ordering = ['name']
        
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

class InventoryDeliveryRecord(models.Model):
    delivery = models.ForeignKey(Delivery, on_delete=models.PROTECT)
    inventory = models.ForeignKey(Inventory, on_delete=models.PROTECT)
    quantity = models.IntegerField()
    unit_order_price = models.IntegerField()
    user_created = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    date_created = models.DateField(auto_now_add=True, blank=True)
