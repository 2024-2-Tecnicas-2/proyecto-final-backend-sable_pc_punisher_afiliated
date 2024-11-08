from django import forms
from .models import Client


class LoginForm(forms.ModelForm):
    
    
    class Meta: 
        model = Client
        fields = ['email', 'password','address','phone']