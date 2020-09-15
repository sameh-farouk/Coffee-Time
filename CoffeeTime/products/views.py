from django.shortcuts import render

# Create your views here.
from .models import CoffeeMachine, CoffeePod
from rest_framework import viewsets, mixins
from .serializers import CoffeeMachineSerializer, CoffeePodSerializer
from django_filters.rest_framework import DjangoFilterBackend

class CoffeeMachineViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint  allows users to be viewed or edited.
    """
    queryset = CoffeeMachine.objects.all()
    serializer_class = CoffeeMachineSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['product_type', 'water_line_compatible']

class CoffeePodViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint  allows users to be viewed or edited.
    """
    queryset = CoffeePod.objects.all()
    serializer_class = CoffeePodSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['product_type', 'flavor', 'pack_size']
