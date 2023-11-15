from django.db import models

# Create your models here.

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

DELIVERY_TYPE_CHOICEFIELD = (
    ('default', 'Default'),
    ('cold-chain', 'Cold Chain'),
    ('third-party', 'Third Party')
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
    sku = models.IntegerField()
    brand = models.CharField(max_length=1000)
    vendor = models.CharField(max_length=1000)
    delivery_type = models.CharField(max_length=48, choices=DELIVERY_TYPE_CHOICEFIELD)
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

    



