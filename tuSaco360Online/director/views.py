from django.shortcuts import render, redirect
from login.models import *

# Create your views here.
def dashboard_pedido(request):
    clientes = Client.objects.all()
    estampados = PrintDesign.objects.all()
    sacos = Hoodie.objects.all()
    sacosEstampados = HoodiePrintDesign.objects.all()
    pedidos = Order.objects.all()
    sacosPedidos = HoodieOrder.objects.all()
    
    # Obtener el id del pedido que se está editando desde la URL (si existe)
    editing_pedido_id = request.GET.get('editing', None)

    # Comprobar si se hace una solicitud POST para actualizar el estado
    if request.method == 'POST':
        pedido_id = request.POST.get('pedido_id')
        nuevo_estado = request.POST.get('status')

        # Buscar el pedido y actualizar su estado
        try:
            pedido = Order.objects.get(id=pedido_id)
            pedido.status = nuevo_estado
            pedido.save()

            # Redirigir a la misma página para reflejar los cambios
            return redirect('dashboard_pedido')

        except Order.DoesNotExist:
            pass

    
    return render(request, 'dashboard.html', 
                  context={
                      'clientes':clientes,
                      'estampados': estampados,
                      'sacos': sacos,
                      'sacosEstampados': sacosEstampados,
                      'pedidos': pedidos,
                      'sacosPedidos': sacosPedidos,
                      'editing_pedido_id': editing_pedido_id  # Enviar el id del pedido que está siendo editado
                  }) 