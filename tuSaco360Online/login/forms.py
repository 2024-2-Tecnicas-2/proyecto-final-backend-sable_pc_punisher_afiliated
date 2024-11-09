from django import forms
from .models import Client  # Usamos el modelo personalizado Client

class LoginForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Client 
        fields = ['username', 'email', 'password', 'name', 'address', 'phone']  

    def save(self, commit=True):
        client = super().save(commit=False)
        client.set_password(self.cleaned_data['password'])  # Encriptamos la contraseña
        if commit:
            client.save()
        return client


class formularioLogin(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)