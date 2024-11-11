from django.shortcuts import render
from login.models import *

def misPedidos(request):
    clientes = Client.objects.all()
    estampados = PrintDesign.objects.all()
    sacos = Hoodie.objects.all()
    sacosEstampados = HoodiePrintDesign.objects.all()
    pedidos = Order.objects.all()
    sacosPedidos = HoodieOrder.objects.all()
    
    # Renderizar la vista del cliente sin opciones de edición
    return render(request, 'misPedidos.html', 
                  context={
                      'clientes': clientes,
                      'estampados': estampados,
                      'sacos': sacos,
                      'sacosEstampados': sacosEstampados,
                      'pedidos': pedidos,
                      'sacosPedidos': sacosPedidos,
                  })
