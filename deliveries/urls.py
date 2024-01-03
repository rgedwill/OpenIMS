from django.urls import path
from deliveries import views

urlpatterns = [
    path('', views.DeliveryList.as_view()),
    path('<int:pk>/', views.DeliveryDetail.as_view()),

]