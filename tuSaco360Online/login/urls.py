from django.urls import path
from .views import home, signin, signup, signout

urlpatterns = [
    path('', home, name='home'),  # La vista 'home' está mapeada a la raíz
    path('signin/', signin, name='signin'),
    path('signup/', signup, name='signup'),
    path('signout/', signout, name='signout'),
    # Asegúrate de que todas las vistas estén mapeadas correctamente
]
