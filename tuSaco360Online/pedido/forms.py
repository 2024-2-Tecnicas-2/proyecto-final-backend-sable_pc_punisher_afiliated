from django import forms
from login.models import *

class HoodieWithImageForm(forms.ModelForm):
    # Definimos un campo para la imagen (especificamente para la imagen del PrintDesign)
    picture = forms.ImageField(required=False)  # Hacemos que el campo de imagen sea opcional

    class Meta:
        model = Hoodie
        fields = ['clothType', 'color', 'size', 'details', 'print', 'hood', 'pocket','picture']

