from django import forms 
from login.models import * 


class HoodieWithImageForm(forms.ModelForm):
    
    class Meta:
        model = Hoodie
        fields = ['clothType', 'color', 'size', 'details', 'print', 'hood', 'pocket']
        
