from django.urls import path
from .views import home, signin, signup, signout

urlpatterns = [
    path('', home, name='home'),  
    path('signin/', signin, name='signin'),
    path('signup/', signup, name='signup'),
    path('signout/', signout, name='signout'),
    
]
