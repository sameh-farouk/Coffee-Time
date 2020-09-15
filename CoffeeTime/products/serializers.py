from .models import CoffeeMachine, CoffeePod
from rest_framework import serializers

class CoffeeMachineSerializer(serializers.HyperlinkedModelSerializer):
    product_type = serializers.ReadOnlyField(source='product_type.name')
    model = serializers.ReadOnlyField(source='product_type.name')

    class Meta:
        model = CoffeeMachine
        fields = ['sku', 'product_type', 'model', 'water_line_compatible']

class CoffeePodSerializer(serializers.HyperlinkedModelSerializer):
    product_type = serializers.ReadOnlyField(source='product_type.name')
    flavor = serializers.ReadOnlyField(source='flavor.name')
    pack_size = serializers.ReadOnlyField(source='pack_size.name')

    class Meta:
        model = CoffeeMachine
        fields = ['sku', 'product_type', 'flavor', 'pack_size']