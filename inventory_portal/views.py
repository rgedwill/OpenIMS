from django.shortcuts import render

from rest_framework.renderers import TemplateHTMLRenderer
from inventory.models import Inventory
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import mixins
from rest_framework import generics

# Create your views here.
class InventoryPortal(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'inventory_portal/inventory_list.html'

    def get(self, request):
        queryset = Inventory.objects.all()
        return Response({'inventory': queryset})

        

def t_inventory_portal_test(request):
    return HttpResponse("success")
    # return render(request, 'inventory_portal/inventory_test.html', {})