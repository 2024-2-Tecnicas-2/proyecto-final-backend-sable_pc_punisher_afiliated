from django.shortcuts import render

# Create your views here.
def dashboard_pedido(request):
    return render(request, 'dashboard') 