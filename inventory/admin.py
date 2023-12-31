from django.contrib import admin
from .models import *
from import_export.admin import ImportExportMixin

class InventoryAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ('name', 'sku', 'brand', 'vendor', 'delivery_type', 'unit_delivery_quantity', 'sale_price')
    
class LocationAdmin(admin.ModelAdmin):
    pass

class UnitAdmin(admin.ModelAdmin):
    pass

class DeliveryTypeAdmin(admin.ModelAdmin):
    readonly_fields = [
        'next_delivery_date'
    ]

admin.site.register(Inventory, InventoryAdmin)
admin.site.register(Location, LocationAdmin)
admin.site.register(Unit, UnitAdmin)
admin.site.register(DeliveryType, DeliveryTypeAdmin)