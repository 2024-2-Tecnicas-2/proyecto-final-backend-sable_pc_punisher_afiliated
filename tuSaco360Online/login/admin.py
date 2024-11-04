from django.contrib import admin
from .models import *
# Register your models here.


class OrderAdmin(admin.ModelAdmin):
    list_display=('id', 'client', 'creationDate', 'finalPrice', 'status')
    list_filter=('status', 'creationDate')
    search_fields = ('client__username', 'client__email')
    ordering = ['creationDate']
    


admin.site.register(Client)
admin.site.register(PrintDesign)
admin.site.register(Hoodie)
admin.site.register(HoodieOrder)
admin.site.register(HoodiePrintDesign)
admin.site.register(Order, OrderAdmin)