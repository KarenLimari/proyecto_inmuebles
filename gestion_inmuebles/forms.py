from django import forms
from .models import User

# Mantenemos los tipos de usuario fuera de la clase User
TIPOS_USUARIOS = [
    ('Arrendatario', 'Arrendatario'),
    ('Arrendador', 'Arrendador'),
]

class TipoUsuarioForm(forms.ModelForm):
    tipo_usuario = forms.ChoiceField(choices=TIPOS_USUARIOS)

    class Meta:
        model = User
        fields = ['tipo_usuario']  # solo el campo tipo_usuario, si es necesario
