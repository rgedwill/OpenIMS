from django.shortcuts import render

from rest_framework.renderers import TemplateHTMLRenderer
from inventory.models import Inventory
from deliveries.models import DeliveryType
from inventory.serializers import InventorySerializer, InventoryDeliveryRecordSerializer
from rest_framework.views import APIView
from rest_framework.response import Response

#purely for that test function which can be deleted
from django.http import HttpResponse

# Create your views here.
class InventoryPortal(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'inventory_portal/inventory.html'

    def get(self, request):
        
        # prefetch inventorydeliveryrecords
        inventory_data = Inventory.objects\
            .select_related('delivery_type')\
            .all()
        # serialize all inventory and related data
        serializer = InventorySerializer(inventory_data)

        delivery_type_data = [d for d in DeliveryType.objects.values()]
        
        # serializer mostly only needed for a form
        return Response(
            {
                'inventory': inventory_data,
                'delivery_type_data': delivery_type_data,
             })

class InventoryListDetail(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'inventory_portal/inventory-list-detail.html'

    def get(self, request, pk):
        print(pk)
        i = Inventory.objects.filter(id=pk).values().first()
        return Response(
            {'inventory_detail': i}
        )

def t_inventory_portal_test(request):
    return HttpResponse("success")
    return render(request, 'inventory_portal/inventory_test.html', {})