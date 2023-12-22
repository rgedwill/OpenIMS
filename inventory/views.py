from django.shortcuts import render

from rest_framework import status, generics
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.renderers import TemplateHTMLRenderer
from django.http import Http404
from rest_framework.response import Response
from inventory.models import Inventory, InventoryDeliveryRecord
from inventory.serializers import InventorySerializer


class InventoryList(generics.ListCreateAPIView):
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer


class InventoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer

class InventoryPortal(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'inventory/inventory_list.html'

    def get(self, request):
        queryset = Inventory.objects.all()
        return Response({'inventory': queryset})

class InventoryDeliveryRecordList(generics.ListCreateAPIView):
    queryset = InventoryDeliveryRecord.objects.all()
    serializer_class = InventorySerializer