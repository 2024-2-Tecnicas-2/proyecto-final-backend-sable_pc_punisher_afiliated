from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .forms import LoginForm, formularioLogin


def home(request):
    if request.user.is_authenticated:
        return redirect('misPedidos')  
    return render(request, 'home.html')


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





def signout(request):
    logout(request)
    return redirect('home')