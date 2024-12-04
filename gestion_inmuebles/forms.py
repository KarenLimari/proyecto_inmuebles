from django import forms
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from .models import User, Perfil, Inmueble, ImagenInmueble, Comuna


# Formulario para la creación personalizada de usuario
class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "password1", "password2", "rut")


# Formulario para seleccionar el tipo de usuario
TIPOS_USUARIOS = [
    ("Arrendatario", "Arrendatario"),
    ("Arrendador", "Arrendador"),
]


class TipoUsuarioForm(forms.Form):
    tipo_usuario = forms.ChoiceField(choices=TIPOS_USUARIOS)


# Formulario para editar el perfil del usuario
class PerfilForm(forms.ModelForm):
    class Meta:
        model = Perfil
        fields = ["direccion", "telefono"]  # Los campos que el usuario puede editar

        # Opcional: personalizar los widgets para mejorar la apariencia
        widgets = {
            "direccion": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Dirección"}
            ),
            "telefono": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Teléfono"}
            ),
        }


# Formulario para cambiar la contraseña
class CustomPasswordChangeForm(PasswordChangeForm):
    class Meta:
        model = User
        fields = ["password", "new_password1", "new_password2"]


class PublicarInmuebleForm(forms.ModelForm):
    class Meta:
        model = Inmueble
        fields = [
            'nombre', 'descripcion', 'm2_construidos', 'm2_totales', 'estacionamientos', 
            'habitaciones', 'banos', 'direccion', 'comuna', 'tipo_inmueble', 'precio_mensual'
        ]
        
        widgets = {
            'descripcion': forms.Textarea(attrs={'rows': 4, 'class': 'form-control'}),
            'precio_mensual': forms.NumberInput(attrs={'class': 'form-control'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'comuna': forms.Select(attrs={'class': 'form-control'}),
            'region': forms.Select(attrs={'class': 'form-control'}),
            'tipo_inmueble': forms.Select(attrs={'class': 'form-control'}),
            'm2_construidos': forms.NumberInput(attrs={'class': 'form-control'}),
            'm2_totales': forms.NumberInput(attrs={'class': 'form-control'}),
            'estacionamientos': forms.NumberInput(attrs={'class': 'form-control'}),
            'habitaciones': forms.NumberInput(attrs={'class': 'form-control'}),
            'banos': forms.NumberInput(attrs={'class': 'form-control'}),
        }
class ImagenInmuebleForm(forms.ModelForm):
    class Meta:
        model = ImagenInmueble
        fields = ['imagen', 'imagen_url']  # Permite subir imagen o usar una URL.