from django import forms
from .models import PerfilUsuario
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ExtendedUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "password1", "password2", "first_name", "last_name", "email"]


class PerfilUsuarioForm(forms.ModelForm):
    class Meta:
        model = PerfilUsuario   #el modelo para el que estamos creando el form es PerfilUsuario
        fields = ["fechaNacimiento", "direccion"]