from django.shortcuts import render
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from deliveries.models import Delivery
# Create your views here.
class DeliveriesPortal(generics.RetrieveUpdateDestroyAPIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'deliveries_portal/deliveries.html'

    def get(self, request):
        queryset = Delivery.objects.all()
        return Response({'deliveries': queryset})