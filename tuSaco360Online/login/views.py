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
    return render(request, 'registration/signin.html', {
        'form':  formularioLogin
    })


# la funcionalidad de cerra sesion borrando los datos de autenticación (Hay un error en la base de datos que llegan dos valores al tiempo)
def signout(request):
    logout(request)
    return redirect('home')


