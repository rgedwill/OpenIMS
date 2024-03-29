"""
URL configuration for openIMS project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from . import views

from django.contrib import admin
from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns

from testapp.views import create_contact, delete_contact, ContactList

urlpatterns = [
    path('', views.base_view),
    path('admin/', admin.site.urls),
    path('create-contact/', create_contact, name='create-contact'),
    path("contacts/", ContactList.as_view(), name='contact-list'),
    path('delete-contact/<int:pk>/', delete_contact, name='delete-contact'),
    path('api-auth/', include('rest_framework.urls')), 
    path('accounts/', include("django.contrib.auth.urls")),

    # DISPLAY
    path('portal/inventory/', include('inventory_portal.urls')),
    path('portal/deliveries/', include('deliveries_portal.urls')),

    
    #API
    path('inventory/', include('inventory.urls')),
    path('deliveries/', include('deliveries.urls')),
]
