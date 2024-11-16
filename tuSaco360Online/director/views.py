from django.shortcuts import render, redirect
from login.models import *
from django.http import HttpResponse

# Create your views here.
def dashboard_pedido(request):
    clientes = Client.objects.all()
    estampados = PrintDesign.objects.all()
    sacos = Hoodie.objects.all()
    sacosEstampados = HoodiePrintDesign.objects.all()
    pedidos = Order.objects.all()
    sacosPedidos = HoodieOrder.objects.all()
    
    # Obtener el id del pedido que se está editando desde la URL (si existe)
    editingPedidoId = request.GET.get('editing', None)
    editingPedidoId = request.GET.get('editing', None)
    if editingPedidoId:
        try:
            editingPedidoId = int(editingPedidoId)  # Convierte a entero
        except ValueError:
            editingPedidoId = None  # Maneja el caso de valores no numéricos

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
            return redirect('dashboard')

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
                      'editingPedidoId': editingPedidoId  # Enviar el id del pedido que está siendo editado
                  }) 


def guardar_pedido(request, pedido_id):
    return HttpResponse("Pedido actualizado")