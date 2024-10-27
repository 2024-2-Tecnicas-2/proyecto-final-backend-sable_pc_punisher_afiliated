from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.db import IntegrityError
# Create your views here.

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
                return HttpResponse('User create succesful')
            except:
                return render(request, 'signup.html', {
                    'form': UserCreationForm,
                    "Error": 'Username already exists'
                })
        return render(request, 'signup.html', {
            'form': UserCreationForm,
            "error": 'Password do not match'
        })

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
                return redirect('personalizacionDePedido')
            except IntegrityError:
                return render(request, 'signup.html', {
                    'error': "Usuario ya existente"
                })

        return render(request, 'signup.html', {
            'form': UserCreationForm,
            'error': "Contraseña incorrecta"
        })
