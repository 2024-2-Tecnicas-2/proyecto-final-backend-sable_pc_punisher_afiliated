from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
#from django.contrib.auth import login, logout, authenticate
# from django.db import IntegrityError
from .forms import HoodieWithImageForm
from login.models import PrintDesign

# Create your views here.


def dashboard_pedido(request):
    return render(request, 'dashboard.html')


def actualizar_pedido(request):
    return render(request, 'actualizacion_estado.html')

    # Esto debe ir creeado en la app de Pedido, ya que la personalización del saco hace parte del pedido.
# Tambien hay que crear los modelos en pedido para que el formulario en fomrs.py queden con las tablas de la base de datos.
# Cambiar tambien la personalizacionSaco.html para pedido en templates.


def hoodieForm(request):
    if request.method == 'POST':
        form = HoodieWithImageForm(request.POST, request.FILES)

        if form.is_valid():
            # Guardamos los datos del saco (Hoodie)
            hoodie_instance = form.save()

            # Si se sube una imagen, guardamos el modelo PrintDesign
            picture = form.cleaned_data.get('picture')
            if picture:
                # Creamos una nueva instancia de PrintDesign
                print_design = PrintDesign(
                    hoodie=hoodie_instance, picture=picture)
                print_design.save()

            # O donde quieras redirigir después de guardar
            return redirect('hoodie')
        else:
            return render(request, 'personalizacionSaco.html', {'form': form, 'error': 'Formulario inválido,, por favor revisa los campos.'})

    else:
        form = HoodieWithImageForm()

    return render(request, 'personalizacionSaco.html', {'form': form})
