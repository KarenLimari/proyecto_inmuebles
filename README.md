# Proyecto Django: Desafío - Manejo de CRUD con Django y PostgreSQL

Este proyecto tiene como objetivo la creación de una plataforma web utilizando **Django** como framework y **PostgreSQL** como motor de base de datos. El proyecto simula una aplicación de arriendo de inmuebles, en la cual se gestionan usuarios, arrendadores, arrendatarios y propiedades.

## Requerimientos Técnicos

- **Motor de base de datos:** PostgreSQL
- **Framework web:** Django
- **Entorno de Python:** Virtual environment (opcional, pero recomendado)
- **Paquete adicional:** python-dotenv para manejar variables de entorno

## Instrucciones de Desarrollo

### 1. Instalación y configuración del motor de base de datos PostgreSQL

1. Instalar PostgreSQL en el sistema.
2. Crear una base de datos llamada `proyecto_inmuebles`:
   ```sql
   CREATE DATABASE proyecto_inmuebles;
   ```

### 2. Configuración del Proyecto Django

1. Crear el proyecto Django
```sql
django-admin startproject proyecto_inmuebles
```
2. Crear la aplicación dentro del proyecto:
```sql
python manage.py startapp gestion_inmuebles
```
3. Configurar la conexión a PostgreSQL en el archivo settings.py
```sql
DATABASES = {
 'default': {
 'ENGINE': 'django.db.backends.postgresql',
 'NAME': os.getenv('DB_NAME'),
 'USER': os.getenv('DB_USER'),
 'PASSWORD': os.getenv('DB_PASSWORD'),
 'HOST': os.getenv('DB-HOST', 'localhost'),
 'PORT': os.getenv('DB_PORT', '5432'),
 }
}

```
### 3. Creación del Modelo y Migraciones

1. Definir el modelo en el archivo models.py de la aplicación testdb:
```sql
from django.db import models

class Inmueble(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    m2_construidos = models.FloatField()
    m2_totales = models.FloatField()
    estacionamientos = models.IntegerField()
    habitaciones = models.IntegerField()
    banos = models.IntegerField()
    direccion = models.CharField(max_length=200)
    comuna = models.CharField(max_length=100)
    tipo_inmueble = models.CharField(max_length=50)
    precio_mensual = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nombre
```
2. Generar las migraciones:

```sql
python manage.py makemigrations
```

3. Aplicar las migraciones:

```sql
python manage.py migrate
```

### 4.Verificación en consola de Postgres

1. Acceder a SQL Shell y verificar la creación de la base de datos.

2. Confirmar la existencia de la tabla personalizada gestion_inmuebles_inmueble y las tablas generadas automáticamente por Django (auth_user, django_migrations, etc.).

3. Captura: Se incluye imágenes de la vista, con las tablas correctamente creadas.

## 5. Capturas  

Las capturas solicitadas están en la carpeta capturas.

### Hito 1: Conexión de Django con PostgreSQL y Creación del Modelo
El Hito 1 cubre los siguientes puntos:

1. Instalación y configuración del entorno de desarrollo.
2. Conexión de Django a la base de datos PostgreSQL usando las variables de entorno.
3. Definición y creación del modelo Inmueble en la aplicación gestion_inmuebles.
4. Ejecución de migraciones para reflejar los cambios en la base de datos.

## Autor  
**Karen Limarí**
