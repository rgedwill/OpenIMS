from django.contrib import admin
from .models import Delivery, DeliveryType

# Register your models here.
class DeliveryAdmin(admin.ModelAdmin):
    list_display = ('created_date', 'delivery_date', 'delivery_type')
    
class DeliveryTypeAdmin(admin.ModelAdmin):
    readonly_fields = [
        'next_delivery_date'
    ]
admin.site.register(Delivery, DeliveryAdmin)
admin.site.register(DeliveryType, DeliveryTypeAdmin)
