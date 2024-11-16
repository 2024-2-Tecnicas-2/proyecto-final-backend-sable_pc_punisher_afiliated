from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class Client(AbstractUser):
    name = models.CharField(max_length=100, null=False, blank=False)
    email = models.EmailField(null=False, blank=False, unique=True)
    address = models.CharField(max_length=100, null=False, blank=False)
    phone = models.CharField(max_length=10, null=False, blank=False)

class PrintDesign(models.Model):
    picture = models.ImageField(upload_to='estampados/')#REVISAR BIEN ESTA OPCION, SOLO DEJA UNA IMAGEN
    class PictureSize(models.TextChoices):
        VEINTEPORCUARENTA = '20x20'
        VEINTEPORVEINTE = '20x40'
    pictureSize = models.CharField(max_length=5, choices=PictureSize, null=False,blank=False)
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
    print = models.BooleanField(default=False)
    hood = models.BooleanField(null=False, default=False )
    pocket = models.BooleanField(null=False , default=False)
    price = models.FloatField(default=0)
    PrintDesign = models.ManyToManyField(PrintDesign, through='HoodiePrintDesign')
    def calcularPrecio(self):
        if(self.clothType == 'Algodón Perchado' and self.hood and self.pocket):
            self.price = 120000
        elif(self.clothType == 'Algodón Perchado' and (not self.hood or not self.pocket)):
            self.price = 110000
        elif(self.clothType == 'Algodón Perchado' and not self.hood and not self.pocket):
            self.price = 95000
        elif(self.clothType == 'Burda' and self.hood and self.pocket):
            self.price = 140000
        elif(self.clothType == 'Burda' and (not self.hood or not self.pocket)):
            self.price = 125000
        elif(self.clothType == 'Burda' and not self.hood and not self.pocket):
            self.price = 110000
            
        estampados = HoodiePrintDesign.objects.filter(hoodie=self)
        # Obtener estampados asociados, se toman los registros de la tabla intermedia y mediante objects, se filtra para obtener solo registros
        #que corresponden con el hoodie actual, tomando asi solo las imagenes asociados al hoodie actual
        if(estampados.exists()):
            
            # Contar estampados de cada tamaño, con la lista de instancias hoodiePrintDesign que coinciden con el hoodie actual, se filtra
            #mediante el atributo de pictureSize y se filtra por cada una de las dos opciones y se hace el conteo
            count_20x20 = estampados.filter(print_design__pictureSize='20x20').count()
            count_20x40 = estampados.filter(print_design__pictureSize='20x40').count()
            # Calcular el precio adicional por estampados
            self.price += count_20x20 * 15000  # Cada estampado 20x20 cuesta 15000
            self.price += count_20x40 * 35000  # Cada estampado 20x40 cuesta 35000
        
        

        

    def save(self, *args, **kwargs):#Se pone *args y **kwargs para que no haya conflicto con los argumentos que utiliza django por defecto al momento de guardar en la DB
        if not self.pk:  # Verifica si el objeto no ha sido guardado
            super().save(*args, **kwargs)  # Guarda inicialmente el objeto para obtener un ID

        self.calcularPrecio()  # Calcula el precio después de guardar
        super().save(*args, **kwargs)  # Guarda nuevamente con el precio actualizado

                
    
    
class HoodiePrintDesign(models.Model):
    hoodie = models.ForeignKey(Hoodie, on_delete=models.CASCADE, null=False)
    print_design = models.ForeignKey(PrintDesign, on_delete=models.CASCADE, null=False)
    #cantidad = models.PositiveBigIntegerField() se retira, no es necesario en este punto, la cantidad se especifica en hoodie order


class Order(models.Model):
    creationDate = models.DateField(auto_now_add=True,null=False)
    finalPrice = models.FloatField(null=False)
    hoodie = models.ManyToManyField(Hoodie, through='HoodieOrder')
    deliveryDate = models.DateField()
    class Status(models.TextChoices):
        PENDIENTE = 'Pd'
        ENVIADO = 'Ev'
        COMPLETADO = 'Ct'
        CANCELADO = 'Cd'
    status = models.CharField(default="Pendiente", null=False, max_length=2, choices=Status)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, null=False)
    class Meta:
        ordering = ['creationDate']#para ordenar por fecha
        
 
class HoodieOrder(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=False)
    hoodie = models.ForeignKey(Hoodie, on_delete=models.CASCADE, null=False)
    cantidad = models.PositiveIntegerField(null=False)
