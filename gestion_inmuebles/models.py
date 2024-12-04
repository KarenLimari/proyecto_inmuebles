from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.text import slugify


TIPOS_INMUEBLES = [
    ('Casa', 'Casa'),
    ('Departamento', 'Departamento'),
    ('Parcela', 'Parcela'),
]
TIPOS_USUARIOS = [
    ('Arrendatario', 'Arrendatario'),
    ('Arrendador', 'Arrendador'),
]
class User(AbstractUser):  
    rut = models.CharField(max_length=12, unique=True)  # Ejemplo: "12345678-9"
    direccion = models.CharField(max_length=200)
    telefono = models.CharField(max_length=15)
    tipo_usuario = models.CharField(max_length=20,choices=TIPOS_USUARIOS)

    def __str__(self):
        return f"{self.username} ({self.tipo_usuario})"
class Region(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Comuna(models.Model):
    nombre = models.CharField(max_length=100)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

class TipoInmueble(models.Model):
    tipo = models.CharField(max_length=200, choices=TIPOS_INMUEBLES)

    def __str__(self):
        return self.tipo

class Inmueble(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    m2_construidos = models.FloatField()
    m2_totales = models.FloatField()
    estacionamientos = models.IntegerField()
    habitaciones = models.IntegerField()
    banos = models.IntegerField()
    direccion = models.CharField(max_length=200)
    comuna = models.ForeignKey(Comuna, on_delete=models.CASCADE)  # Relacion con Comuna
    tipo_inmueble = models.ForeignKey(TipoInmueble, on_delete=models.SET_NULL, null=True)
    region = models.ForeignKey(Region, on_delete=models.CASCADE, null=True)  # Permitir null
    precio_mensual = models.DecimalField(max_digits=10, decimal_places=2)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.nombre)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.nombre
    
class ImagenInmueble(models.Model):
    inmueble = models.ForeignKey(Inmueble, related_name='imagenes', on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='inmuebles/', null=True, blank=True)
    imagen_url = models.URLField(null=True, blank=True)  # Si no se sube imagen, permite una URL.

    def __str__(self):
        return f"Imagen de {self.inmueble.nombre}"
# Modelo Perfil relacionado con el usuario

class Perfil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    direccion = models.CharField(max_length=255, default='')  # Valor por defecto vacío
    telefono = models.CharField(max_length=15, default='')  # Valor por defecto vacío

    def __str__(self):
        return f"Perfil de {self.user.username}"
