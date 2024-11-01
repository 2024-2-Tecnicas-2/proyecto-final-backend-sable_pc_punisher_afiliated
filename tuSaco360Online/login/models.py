from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class Client(AbstractUser):
    name = models.CharField(max_length=100, null=False, blank=False)
    email = models.EmailField(null=False, blank=False)
    address = models.CharField(max_length=100, null=False, blank=False)
    phone = models.CharField(max_length=10, null=False, blank=False)

class PrintDesign(models.Model):
    picture = models.ImageField(upload_to='estampados/')#REVISAR BIEN ESTA OPCION, SOLO DEJA UNA IMAGEN 
    pictureSize = models.CharField(max_length=50)
    location = models.TextField()

class Hoodie(models.Model):
    class ClothType(models.TextChoices):
        COTTON = 'Algodón Perchado'
        BURDA = 'Burda'

    clothType= models.CharField(max_length=17, choices=ClothType, null=False, blank=False)
    color = models.CharField(max_length=15, null=False, blank=False)
    class Size(models.TextChoices):
        SMALL = 'S'
        MEDIUM = 'M'
        LARGE = 'L'
        EXTRA_LARGE = 'XL'
        DOUBLE_EXTRA_LARGE = 'XXL'
    
    size = models.CharField(max_length=3, null=False, blank=False, choices=Size)
    details = models.TextField()
    print = models.BooleanField(null=False, blank=False)
    hood = models.BooleanField(null=False, blank=False)
    price = models.FloatField(null=False)
    
class HoodiePrintDesign(models.Model):
    hoodie = models.ForeignKey(Hoodie, on_delete=models.CASCADE, null=False)
    print_design = models.ForeignKey(PrintDesign, on_delete=models.CASCADE, null=False)
    cantidad = models.PositiveBigIntegerField()


class Order(models.Model):
    creationDate = models.DateField(auto_now_add=True,null=False)
    finalPrice = models.FloatField(null=False)
    hoodie = models.ManyToManyField(Hoodie, through='HoodieOrder', null=False)
    deliveryDate = models.DateField()
    status = models.CharField(default="Pendiente", null=False, max_length=30)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, null=False)
    

class HoodieOrder(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=False)
    hoodie = models.ForeignKey(Hoodie, on_delete=models.CASCADE, null=False)
    cantidad = models.PositiveIntegerField(null=False)




