from django.db import models

# Create your models here.

"""
Model for the "profile" of an item. Shows pricing, clearances, sku/upc, etc.
"""
class Inventory(models.Model):
    
    pass
"""
Model for an "instance" of Inventory. It has a simple, loose connection via foreign key, but
functions completely differnetly from Inventory. These items can be moved, counted, duplicated, defected, etc.
"""
class Unit(models.Model):
    pass


"""
Model for a location to put items (units) in.
"""
class Location(models.Model):
    pass
    