from django.urls import path
from .views import hoodieForm

urlpatterns = [
    path('', hoodieForm, name= 'hoodieForm'),
     
    #path('FormHoodieAndPrintDesign/', hoodieForm, name= 'hoodieDesign'),
  ]