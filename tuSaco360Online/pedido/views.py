from django.shortcuts import render, redirect,get_object_or_404
from .forms import HoodieWithImageForm
from login.models import PrintDesign, HoodiePrintDesign, Hoodie
from django.http import HttpResponse

# Create your views here.


def actualizar_pedido(request):
    return render(request, 'actualizacion_estado.html')
# Vista para mostrar el formulario y guardar el hoodie
def hoodieForm(request):
    if request.method == 'POST':
        form = HoodieWithImageForm(request.POST, request.FILES)
        
        if form.is_valid():
            # Crear la instancia de Hoodie
            try:
                hoodie_instance = form.save(commit=False)
                hoodie_instance.save()  # Guardamos el hoodie en la base de datos
                
                # Si se selecciona estampado, redirigir a printDesign
                if form.cleaned_data['print']:
                    return redirect('printDesign', hoodie_id=hoodie_instance.id)
                else:
                    return redirect('misPedidos')
            except Exception as e:
                return render(request, 'personalizacionSaco.html', {'form': form, 'error': f'Error al guardar: {e}'})
        else:
            return render(request, 'personalizacionSaco.html', {'form': form, 'error': 'Formulario inválido. Por favor revisa los campos.'})
    else:
        form = HoodieWithImageForm()

    return render(request, 'personalizacionSaco.html', {'form': form})


# Vista para manejar el diseño del estampado
def printDesign(request, hoodie_id):
    hoodie_instance = get_object_or_404(Hoodie, id=hoodie_id)

    if request.method == 'POST':
        pictures = request.FILES.getlist('pictures')
        picture_size = request.POST.get('pictureSize', '20x20')
        location = request.POST.get('location', 'Frente')

        # Validar datos del estampado
        valid_sizes = ['20x20', '20x40']
        valid_locations = ['Frente', 'Espalda', 'Manga']
        if not pictures:
            return HttpResponse("Por favor, sube al menos una imagen para el estampado.")
        if picture_size not in valid_sizes:
            return HttpResponse("El tamaño seleccionado no es válido.")
        if location not in valid_locations:
            return HttpResponse("La ubicación seleccionada no es válida.")

        # Guardar estampados e asociarlos al hoodie
        try:
            for picture in pictures:
                print_design = PrintDesign(
                    picture=picture,
                    pictureSize=picture_size,
                    location=location
                )
                print_design.save()

                HoodiePrintDesign.objects.create(
                    hoodie=hoodie_instance,
                    print_design=print_design
                )
            return redirect('misPedidos')
        except Exception as e:
            return HttpResponse(f"Error al guardar el estampado: {e}")

    return render(request, 'printDesign.html', {'hoodie': hoodie_instance})