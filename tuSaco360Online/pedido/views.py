from django.shortcuts import render, redirect
from .forms import HoodieWithImageForm
from login.models import PrintDesign, HoodiePrintDesign, Hoodie
from django.shortcuts import render, get_object_or_404


# Create your views here.


def actualizar_pedido(request):
    return render(request, 'actualizacion_estado.html')


def hoodieForm(request):
    if request.method == 'POST':
        form = HoodieWithImageForm(request.POST)

        if form.is_valid():
            # Guardamos el hoodie (esto ya guarda la información del hoodie)
            hoodie_instance = form.save()

            if form.cleaned_data['print'] == True:

                return redirect('printDesign', hoodie_id=hoodie_instance.id)

        else:
            return render(request, 'personalizacionSaco.html', {'form': form, 'error': 'Formulario inválido, por favor revisa los campos.'})

    else:
        form = HoodieWithImageForm()

    return render(request, 'personalizacionSaco.html', {'form': form})


def printDesign(request, hoodie_id):

    hoodie_instance = get_object_or_404(Hoodie, id=hoodie_id)

    # Si hay imágenes, las procesamos
    # Obtenemos todas las imágenes enviadas en el formulario
    pictures = request.FILES.getlist('pictures')

    if not pictures:
        return redirect('pintDesign')

    else:

        for picture in pictures:
            # Creamos una instancia de PrintDesign por cada imagen
            print_design = PrintDesign(
                picture=picture,
                pictureSize='20x20',  # Puedes ajustarlo según necesites
                location='Frente'     # Lo mismo para location
            )
            print_design.save()

            # Asociamos cada PrintDesign al Hoodie
   #         HoodiePrintDesign.objects.create(hoodie=hoodie_instance,  # Este es el hoodie recuperado usando el ID
        #                                     print_design=print_design)

            return redirect('misPedidos')

    return redirect('pintDesign.html')
