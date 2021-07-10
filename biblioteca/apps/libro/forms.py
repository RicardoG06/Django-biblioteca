from django import forms
from .models import Autors

class AutorForm(forms.ModelForm):
    class Meta: #metadatos del formulario
        model = Autors
        fields = ['nombre', 'apellidos', 'nacionalidad']
