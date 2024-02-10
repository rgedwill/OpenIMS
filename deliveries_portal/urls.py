from django.urls import path
from deliveries_portal import views

urlpatterns = [
    path('', views.DeliveriesPortal.as_view()),
    # path('list-detail/<int:pk>', views.DeliveriesPortal.as_view()),
]