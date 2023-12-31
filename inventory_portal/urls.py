from django.urls import path
from inventory_portal import views

urlpatterns = [
    path('', views.InventoryPortal.as_view())
]