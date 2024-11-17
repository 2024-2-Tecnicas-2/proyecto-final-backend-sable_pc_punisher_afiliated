from django.urls import path
from .views import hoodieForm, printDesign
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('FormHoodieAndPrintDesign/', hoodieForm, name= 'hoodieDesign'),
    path('CargarImagen/<int:hoodie_id>/', printDesign, name= 'printDesign'),
        
  ] + static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)