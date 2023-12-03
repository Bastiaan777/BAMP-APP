from django import forms
from .models import PerfilUsuario

class PerfilUsuarioForm(forms.ModelForm):
    class Meta:
        model = PerfilUsuario   #el modelo para el que estamos creando el form es PerfilUsuario
        fields = ["fechaNacimiento", "direccion"]