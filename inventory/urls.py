from django.urls import path
from inventory import views

urlpatterns = [
    path('', views.InventoryList.as_view()),
    path('<int:pk>/', views.InventoryDetail.as_view()),
    path('delivery-record-list/', views.InventoryDeliveryRecordList.as_view()),
    path('delivery-record/<int:pk>', views.InventoryDeliveryRecordDetail.as_view())
]