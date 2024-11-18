from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .forms import LoginForm, formularioLogin


def home(request):
    # Si el usuario está autenticado, lo redirigimos a la página de "misPedidos"
    if request.user.is_authenticated:
        return redirect('misPedidos')

    # Lista de productos (puedes agregar o modificar estos productos como desees)
    products = [
        {'name': 'Saco con capota Negro', 'price': 99000, 'image_url': 'https://http2.mlstatic.com/D_NQ_NP_929738-MCO77136564730_062024-O.webp'},
        {'name': 'Saco sin capota Azul oscuro', 'price': 89999, 'image_url': 'https://majuauniformes.com/wp-content/uploads/2018/04/saco_perchado_capota.jpg'},
        {'name': 'Saco sin capota Azul claro', 'price': 89999, 'image_url': 'https://www.centrodeimpresiones.com/wp-content/uploads/2018/02/051-ROYAL-7.jpg'},
        {'name': 'Buzo sin capota manga larga', 'price': 69900, 'image_url': 'https://majuauniformes.com/wp-content/uploads/2018/04/saco_perchado_sin_capota.jpg'},
        {'name': 'Saco estampado blanco', 'price': 50000, 'image_url': 'https://coloursstreet.co/cdn/shop/products/WhatsAppImage2021-03-09at10.24.44AM_18999db3-1201-4ac2-978d-f2d04dd988c4.jpg'},
        {'name': 'Saco estampado rojo', 'price': 50000, 'image_url': 'https://coloursstreet.co/cdn/shop/products/WhatsAppImage2021-03-09at10.25.04AM.jpg?v=1630184558'},
        {'name': 'Saco estampado negro', 'price': 50000, 'image_url': 'https://coloursstreet.co/cdn/shop/products/unnamed_12.jpg?v=1630184029'},
        {'name': 'Saco sin capota Marrón', 'price': 89900, 'image_url': 'https://hmecuador.vtexassets.com/arquivos/ids/1618575/Sudadera-Loose-Fit---Marron---H-M-EC.jpg?v=638446306451730000'}
    ]

    # Renderizar el template home.html pasando la lista de productos
    return render(request, 'home.html', {'products': products})


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