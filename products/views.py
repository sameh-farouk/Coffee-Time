from django.shortcuts import render

# Create your views here.
from .models import CoffeeMachine, CoffeePod, CoffeeMachineType, CoffeePodType, CoffeePodFlavor, CoffeePodPacksize
from rest_framework import viewsets, mixins
from .serializers import CoffeeMachineSerializer, CoffeePodSerializer
from django_filters.rest_framework import DjangoFilterBackend


class CoffeeMachineViewSet(mixins.ListModelMixin ,viewsets.GenericViewSet):
    """
    API endpoint  return the JSON data for all coffee machines products filterable by product type, water line.
    """
    queryset = CoffeeMachine.objects.all()
    serializer_class = CoffeeMachineSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['product_type__name', 'water_line_compatible']


class CoffeePodViewSet(mixins.ListModelMixin ,viewsets.GenericViewSet):
    """
    API endpoint  return the JSON data for all the coffee pods products filterable by product type, coffee flavor, and pack size.
    """
    queryset = CoffeePod.objects.all()
    serializer_class = CoffeePodSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['product_type__name', 'flavor__name', 'pack_size__dozen']
