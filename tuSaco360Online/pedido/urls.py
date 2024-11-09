from django.urls import path
from .views import hoodieForm

urlpatterns = [
    path('FormHoodieAndPrintDesign/', hoodieForm, name= 'hoodieDesign'),
  ]