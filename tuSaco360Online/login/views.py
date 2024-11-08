from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
# from django.db import IntegrityError
# from .forms import HoodieWithImageForm
from .models import PrintDesign
from .forms import LoginForm


def home(request):
    return render(request, 'home.html')


def signup(request):
    if request.method == 'POST':

        form = LoginForm(request.POST)

        if form.is_valid():

            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            address = form.cleaned_data['address']
            phone = form.cleaned_data['phone']


            new_client = form.save()
            
            
            # Hacer la validacion de si es admin o cliente:
           
            
            
            return redirect('home',{
                'title': "Ingrese a inciar sesion para logearse "
            })

    else:

        form = LoginForm()

    return render(request, 'registration/signup.html', 
                  {'form': form, 'error': "el formulario no es valido,por favor validar los datos del formulario e intente de nevo"})


def signin(request):
    formularioLogin = LoginForm()
    return render(request, 'signin', {
        'form':  formularioLogin
    })


# la funcionalidad de cerra sesion borrando los datos de autenticación (Hay un error en la base de datos que llegan dos valores al tiempo)
def signout(request):
    logout(request)
    return redirect('home')


# Esto debe ir creeado en la app de Pedido, ya que la personalización del saco hace parte del pedido.
# Tambien hay que crear los modelos en pedido para que el formulario en fomrs.py queden con las tablas de la base de datos.
# Cambiar tambien la personalizacionSaco.html para pedido en templates.
""""
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
                print_design = PrintDesign(hoodie=hoodie_instance, picture=picture)
                print_design.save()

            # O donde quieras redirigir después de guardar
            return redirect('hoodie')
        else:
            return render(request, 'personalizacionSaco.html', {'form': form, 'error': 'Formulario inválido,, por favor revisa los campos.'})

    else:
        form = HoodieWithImageForm()

    return render(request, 'personalizacionSaco.html', {'form': form})
"""
