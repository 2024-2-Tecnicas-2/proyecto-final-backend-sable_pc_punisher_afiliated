from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
# from django.db import IntegrityError
# from .forms import HoodieWithImageForm
from .models import PrintDesign
from .forms import LoginForm, formularioLogin


def home(request):
    return render(request, 'home.html')
from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import LoginForm

def signup(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            # Guardar el nuevo cliente (usuario)
            new_client = form.save()

            # Iniciar sesión automáticamente al registrar al cliente
            login(request, new_client)

            # Redirigir al home después de registrar
            return redirect('home')
    else:
        form = LoginForm()

    return render(request, 'registration/signup.html', {'form': form})

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import formularioLogin

def signin(request):
    if request.method == 'POST':
        form = formularioLogin(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            
            # Intentamos autenticar al usuario con username y password
            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                # Si las credenciales son correctas, lo logueamos
                login(request, user)
                return redirect('home')  # Redirigir al home después del login
            else:
                # Si las credenciales son incorrectas
                return render(request, 'registration/signin.html', {
                    'form': form,
                    'error': "Nombre de usuario o contraseña incorrectos."
                })
    else:
        form = formularioLogin()

    return render(request, 'registration/signin.html', {'form': form})




# la funcionalidad de cerra sesion borrando los datos de autenticación (Hay un error en la base de datos que llegan dos valores al tiempo)
def signout(request):
    logout(request)
    return redirect('home')