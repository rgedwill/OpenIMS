from django.shortcuts import render
from rest_framework.renderers import TemplateHTMLRenderer
from inventory.models import Inventory
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
class InventoryPortal(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'inventory_portal/inventory_list.html'

    def get(self, request):
        queryset = Inventory.objects.all()
        return Response({'inventory': queryset})
