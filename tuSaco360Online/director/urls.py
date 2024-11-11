from django.urls import path
from .views import dashboard_pedido #   [Acá impottan todas las funciones o metodos que provienen de views.py ejemplo "home"]

urlpatterns = [
    path('dashboard/',dashboard_pedido, name='dashboard'),  
]