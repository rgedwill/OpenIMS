from django.urls import path
from inventory_portal import views

urlpatterns = [
    path('', views.InventoryPortal.as_view()),
    path('list-detail/<int:pk>', views.InventoryListDetail.as_view()),
    path('test', views.t_inventory_portal_test)
]