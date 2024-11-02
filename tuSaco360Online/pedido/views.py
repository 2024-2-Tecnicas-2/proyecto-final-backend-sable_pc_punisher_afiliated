from django.shortcuts import render

# Create your views here.
def dashboard_pedido(request):
    return render(request, 'dashboard.html') 


def actualizar_pedido(request):
     return render(request, 'actualizacion_estado.html') 