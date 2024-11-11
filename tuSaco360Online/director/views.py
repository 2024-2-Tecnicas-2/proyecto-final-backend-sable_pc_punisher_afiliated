from django.shortcuts import render
from login.models import *
# Create your views here.
def dashboard_pedido(request):
    clientes = Client.objects.all()
    estampados = PrintDesign.objects.all()
    sacos = Hoodie.objects.all()
    sacosEstampados = HoodiePrintDesign.objects.all()
    pedidos = Order.objects.all()
    sacosPedidos = HoodieOrder.objects.all()
    
    return render(request, 'dashboard', 
                  context={
                      'clientes':clientes,
                      'estampados': estampados,
                      'sacos': sacos,
                      'sacosEstampados': sacosEstampados,
                      'pedidos': pedidos,
                      'sacosPedidos': sacosPedidos
                  }) 