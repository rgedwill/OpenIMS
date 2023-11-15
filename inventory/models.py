from django.db import models

# Create your models here.

"""
Model for the "profile" of an item. Shows pricing, clearances, sku/upc, etc.
"""

DELIVERY_TYPE_CHOICEFIELD = (
    ('default', 'Default'),
    ('cold-chain', 'Cold Chain'),
    ('third-party', 'Third Party')
)

class Inventory(models.Model):
    name = models.CharField(max_length=2000)
    sku = models.IntegerField()
    brand = models.CharField(max_length=1000)
    vendor = models.CharField(max_length=1000)
    delivery_type = models.CharField(max_length=48, choices=DELIVERY_TYPE_CHOICEFIELD)
    unit_delivery_quantity = models.IntegerField() # how many units are delivered in a full casepack

    # TODO: add function to convert this to decimals. It's better to do it this way according to 
    # https://stackoverflow.com/a/50376841/5877575
    sale_price = models.IntegerField() 

    def __str__(self):
        return self.name


"""
Model for an "instance" of Inventory. It has a simple, loose connection via foreign key, but
functions completely differnetly from Inventory. These items can be moved, counted, duplicated, defected, etc.
"""
class Unit(models.Model):
    # inventory = models.ForeignKey(Inventory, on_delete=PROTECT)
    pass


"""
Model for a location to put items (units) in.
"""
class Location(models.Model):
    pass
