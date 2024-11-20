from django.urls import path
from .views import home, signin, signup, signout, Pedidos

urlpatterns = [
    path('', home, name='home'),
    path('Pedidos/', Pedidos, name='Pedidos'),  
    path('signin/', signin, name='signin'),
    path('signup/', signup, name='signup'),
    path('signout/', signout, name='signout'),
    
]
