from django.urls import path
from inventory import views

urlpatterns = [
    path('', views.InventoryList.as_view()),
    path('<int:pk>/', views.InventoryDetail.as_view()),
    path('delivery-records/', views.InventoryDeliveryRecordList.as_view()),

    path('portal/', views.InventoryPortal.as_view())
]