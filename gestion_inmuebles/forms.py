from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User  # Asegúrate de que este User es el que usas

# Formulario para la creación personalizada de usuario (sin 'tipo_usuario' aquí)
class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2','rut')  # Elimina tipo_usuario de aquí


# Formulario para seleccionar el tipo de usuario
TIPOS_USUARIOS = [
    ('Arrendatario', 'Arrendatario'),
    ('Arrendador', 'Arrendador'),
]

class TipoUsuarioForm(forms.Form):
    tipo_usuario = forms.ChoiceField(choices=TIPOS_USUARIOS)