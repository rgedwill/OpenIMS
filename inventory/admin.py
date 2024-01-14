from django.contrib import admin
from .models import Inventory, InventoryDeliveryRecord, Location, Unit
from deliveries.models import DeliveryType
from import_export.admin import ImportExportMixin

class InventoryAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ('name', 'sku', 'brand', 'vendor', 'delivery_type', 'unit_delivery_quantity', 'sale_price')
    
class InventoryDeliveryRecordAdmin(admin.ModelAdmin):
    list_display = ('delivery', 'inventory', 'quantity', 'unit_order_price', 'user_created', 'date_created')
    
class LocationAdmin(admin.ModelAdmin):
    pass

class UnitAdmin(admin.ModelAdmin):
    pass



admin.site.register(Inventory, InventoryAdmin)
admin.site.register(Location, LocationAdmin)
admin.site.register(Unit, UnitAdmin)
admin.site.register(InventoryDeliveryRecord, InventoryDeliveryRecordAdmin)
# admin.site.register(InventoryDeliveryRecord)