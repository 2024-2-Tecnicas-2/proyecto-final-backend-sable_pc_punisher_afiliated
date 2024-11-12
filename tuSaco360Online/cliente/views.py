from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from login.models import *

@login_required
def misPedidos(request):
    # Filtrar solo los pedidos del cliente que ha iniciado sesión
    pedidos = Order.objects.filter(client=request.user)
    sacosPedidos = HoodieOrder.objects.filter(order__in=pedidos)
    
    estampados = PrintDesign.objects.all()
    sacos = Hoodie.objects.all()
    sacosEstampados = HoodiePrintDesign.objects.all()
    
    return render(request, 'misPedidos.html', 
                  context={
                      'pedidos': pedidos,
                      'sacosPedidos': sacosPedidos,
                      'estampados': estampados,
                      'sacos': sacos,
                      'sacosEstampados': sacosEstampados,
                  })
