from django import forms
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from .models import User, Perfil

# Formulario para la creación personalizada de usuario
class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'rut')

# Formulario para seleccionar el tipo de usuario
TIPOS_USUARIOS = [
    ('Arrendatario', 'Arrendatario'),
    ('Arrendador', 'Arrendador'),
]

class TipoUsuarioForm(forms.Form):
    tipo_usuario = forms.ChoiceField(choices=TIPOS_USUARIOS)

# Formulario para editar el perfil del usuario
class PerfilForm(forms.ModelForm):
    class Meta:
        model = Perfil
        fields = ['direccion', 'telefono']  # Los campos que el usuario puede editar

        # Opcional: personalizar los widgets para mejorar la apariencia
        widgets = {
            'direccion': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Dirección'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Teléfono'})
        }

# Formulario para cambiar la contraseña
class CustomPasswordChangeForm(PasswordChangeForm):
    class Meta:
        model = User
        fields = ['password', 'new_password1', 'new_password2']
