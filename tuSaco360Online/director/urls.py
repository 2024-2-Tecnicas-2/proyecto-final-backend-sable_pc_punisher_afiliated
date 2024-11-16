from django.urls import path
from .views import * #   [Acá impottan todas las funciones o metodos que provienen de views.py ejemplo "home"]

urlpatterns = [
    path('dashboard/',dashboard_pedido, name='dashboard'),  
    path('guardar_pedido/<int:pedido_id>/', guardar_pedido, name='guardar_pedido')
]