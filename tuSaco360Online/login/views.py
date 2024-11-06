from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from .forms import HoodieWithImageForm
from .models import PrintDesign

# Create your views here.


def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html', {
            'form': UserCreationForm

        })

    else:

        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(
                    username=request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('personalizacionSaco.html')
            except IntegrityError:
                return render(request, 'signup.html', {
                    'error': "Usuario ya existente"
                })

        return render(request, 'signup.html', {
            'form': UserCreationForm,
            'error': "Contraseña incorrecta"
        })


def signout(request):
    logout(request)
    return redirect('home')


def signin(request):

    if request.method == 'GET':
        return render(request, 'signin.html', {
            'form': AuthenticationForm
        })
    else:
        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'signin.html', {
                'form': AuthenticationForm,
                'error': 'User Name Or Password Is Incorrect'
            })
        else:
            login(request, user)
            return redirect('personalizacionSaco')


def hoodie_form(request):
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
            return render(request, 'personalizacionSaco.html', {'form': form, 'error': 'Formulario inválido, por favor revisa los campos.'})

    else:
        form = HoodieWithImageForm()

    return render(request, 'personalizacionSaco.html', {'form': form})
