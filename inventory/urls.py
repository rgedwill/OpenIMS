from django.urls import path
from inventory import views

urlpatterns = [
    path('inventory/', views.InventoryList.as_view()),
    path('inventory/<int:pk>/', views.InventoryDetail.as_view()),
]