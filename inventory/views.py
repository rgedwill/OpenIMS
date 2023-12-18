from django.shortcuts import render

from rest_framework import status, generics
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from django.http import Http404
from rest_framework.response import Response
from inventory.models import Inventory
from inventory.serializers import InventorySerializer

class InventoryList(generics.ListCreateAPIView):
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer


class InventoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer