from django.db import models

# Opciones para el tipo de inmueble
TIPOS_INMUEBLES = [
    ('Casa', 'Casa'),
    ('Departamento', 'Departamento'),
    ('Parcela', 'Parcela'),
]

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
    comuna = models.ForeignKey(Comuna, on_delete=models.CASCADE)  # Relacionar con Comuna
    tipo_inmueble = models.ForeignKey(TipoInmueble, on_delete=models.SET_NULL, null=True)
    precio_mensual = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nombre
