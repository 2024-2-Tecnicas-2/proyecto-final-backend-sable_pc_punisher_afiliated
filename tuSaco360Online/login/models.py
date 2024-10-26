from django.db import models
from enum import Enum
# Create your models here.
class Client():
    name = models.CharField(max_length=100, null=False, blank=False)
    email = models.EmailField(null=False, blank=False)
    address = models.CharField(max_length=100, null=False, blank=False)
    phone = models.CharField(max_length=10, null=False, blank=False)

class ClothType(Enum):
    COTTON = 'Algodón Perchado'
    BURDA = 'Burda'


class Hoodie(models.Model):
    color = models.CharField(max_length=15, null=False, blank=False)
    size = models.CharField(max_length=3, null=False, blank=False)
    clothType = models.CharField(max_length=20, choices=[(tipo.name, tipo.value) for tipo in ClothType])
    print = models.BooleanField(null=False, blank=False)
    hood = models.BooleanField(null=False, blank=False)
    price = models.FloatField(null=False)

class Order(models.Model):
    creationDate = models.DateField(auto_now_add=True,null=False)
    finalPrice = models.FloatField(null=False)
    hoodie = models.ManyToManyField(Hoodie, through='HoodieOrder', null=False)

class HoodieOrder(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=False)
    saco = models.ForeignKey(Hoodie, on_delete=models.CASCADE, null=False)
    cantidad = models.PositiveBigIntegerField(null=False)




