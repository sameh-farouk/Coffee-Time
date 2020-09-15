from django.contrib import admin
from .models import CoffeeMachineModel, CoffeeMachineType, CoffeeMachine, CoffeePodFlavor, CoffeePodType, CoffeePodPacksize, CoffeePod


# Register your models here.
admin.site.register(
    [CoffeeMachineModel, CoffeeMachineType, CoffeeMachine, 
    CoffeePodFlavor,  CoffeePodType, CoffeePodPacksize, CoffeePod])
    