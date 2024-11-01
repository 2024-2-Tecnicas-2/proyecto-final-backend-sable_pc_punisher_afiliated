from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
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


def create_bag(request):
    return render(request, 'personalizacionSaco.html') 