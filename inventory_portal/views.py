from django.shortcuts import render

from rest_framework.renderers import TemplateHTMLRenderer
from inventory.models import Inventory
from inventory.serializers import InventorySerializer, InventoryDeliveryRecordSerializer
from rest_framework.views import APIView
from rest_framework.response import Response


# Create your views here.
class InventoryPortal(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'inventory_portal/inventory.html'

    def get(self, request):
        inventory_data = Inventory.objects.prefetch_related('inventorydeliveryrecord_set').all()
        serializer = InventorySerializer(inventory_data)
        return Response({'inventory': inventory_data, 'serializer': serializer})

        

def t_inventory_portal_test(request):
    return HttpResponse("success")
    # return render(request, 'inventory_portal/inventory_test.html', {})