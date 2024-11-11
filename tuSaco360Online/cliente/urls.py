from django.urls import path
from .views import misPedidos

urlpatterns = [
    path('misPedidos/', misPedidos, name='misPedidos')
]
