from django.contrib import admin
from .models import Delivery

# Register your models here.
class DeliveryAdmin(admin.ModelAdmin):
    list_display = ('created_date', 'delivery_date', 'delivery_type')

admin.site.register(Delivery, DeliveryAdmin)