from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Client)
admin.site.register(PrintDesign)
admin.site.register(Hoodie)
admin.site.register(HoodieOrder)
admin.site.register(HoodiePrintDesign)
admin.site.register(Order)