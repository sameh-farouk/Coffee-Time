#from django.db import models
from djongo import models

# Create your models here.
class CoffeeMachineType(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):      
        return self.name


class CoffeeMachineModel(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):      
        return self.name


class CoffeePodType(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):      
        return self.name


class CoffeePodFlavor(models.Model):
    name = models.CharField(max_length=50, unique=True)
    
    def __str__(self):
        return self.name


class CoffeePodPacksize(models.Model):
    name = models.CharField(max_length=50, unique=True)
    dozen = models.IntegerField()

    def __str__(self):
        return self.name


class CoffeeMachine(models.Model):
    sku = models.CharField(max_length=50, unique=True)
    product_type = models.ForeignKey('CoffeeMachineType', on_delete=models.PROTECT)
    model = models.ForeignKey('CoffeeMachineModel', on_delete=models.PROTECT)
    water_line_compatible = models.BooleanField(default=False)
    objects = models.DjongoManager()

    def __str__(self):
        return f'{self.sku} - {self.product_type}, {self.model}{", water line compatible" if self.water_line_compatible else ""}'

class CoffeePod(models.Model):
    sku = models.CharField(max_length=50, unique=True)
    product_type = models.ForeignKey('CoffeePodType', on_delete=models.PROTECT)
    flavor = models.ForeignKey('CoffeePodFlavor', on_delete=models.PROTECT)
    pack_size = models.ForeignKey('CoffeePodPacksize', on_delete=models.PROTECT)
    objects = models.DjongoManager()

    def __str__(self):
        return f'{self.sku} - {self.product_type}, {self.pack_size}, {self.flavor}'