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

### Hito 2: Creación de Relaciones en el Modelo y Verificación de su Funcionamiento
El Hito 2 cubre los siguientes puntos:

1. Definición del Modelo TipoInmueble:

2. Se ha creado un nuevo modelo TipoInmueble con el campo tipo que almacena los diferentes tipos de inmuebles (por ejemplo, "Casa", "Departamento", "Parcela").Este modelo permite categorizar los inmuebles y establecer una relación con el modelo Inmueble.
Modificación del Modelo Inmueble:

3. Se ha añadido una relación de tipo ForeignKey en el modelo Inmueble para asociar cada inmueble con un tipo específico (TipoInmueble).Esto permite que cada inmueble esté relacionado con un tipo de inmueble, y la relación se maneja mediante una clave foránea.
Registro de Modelos en el Panel de Administración:

4. Se han registrado ambos modelos (Inmueble y TipoInmueble) en el panel de administración de Django para facilitar la gestión de estos desde la interfaz web. De esta manera, se pueden crear, editar y eliminar inmuebles y tipos de inmuebles directamente desde el panel de administración.
Pruebas desde el Shell de Django.

5. Se ha validado que el panel de administración de Django muestra correctamente los modelos Inmueble y TipoInmueble.
Además, se ha probado la creación de inmuebles directamente desde la interfaz de administración.

### Hito 2: Autenticación de Usuarios con Django-Auth
Este hito incluye la implementación de un sistema de autenticación de usuarios, gestionando permisos y grupos específicos para arrendadores y arrendatarios.

1. Configuración de la Autenticación
Se configuraron las aplicaciones django.contrib.auth y django.contrib.contenttypes en el archivo settings.py.
Se crearon las URLs para las vistas de autenticación (registro, inicio y cierre de sesión).
Se creó un superusuario para poder acceder al panel de administración de Django.

2. Creación de la Vista y Formulario de Registro
Se implementó el formulario de registro utilizando UserCreationForm.
Se diseñó la vista y el template HTML para el formulario de registro.
Se verificó que los usuarios pueden registrarse correctamente y se les asigna el tipo de usuario (arrendatario o arrendador).

3. Creación de las Vistas de Inicio y Cierre de Sesión
Se crearon las vistas de inicio y cierre de sesión utilizando LoginView y LogoutView.
Se diseñaron los templates HTML para las vistas de inicio y cierre de sesión.
Se comprobó que los usuarios pueden iniciar y cerrar sesión correctamente.

4. Gestión de Permisos y Grupos de Usuarios
Se configuraron permisos específicos para arrendadores y arrendatarios.
Se crearon y asignaron grupos de usuarios con permisos específicos:
Arrendatarios: Permiso para listar propiedades y generar solicitudes de arriendo.
Arrendadores: Permiso para crear, editar, eliminar y listar propiedades, así como aceptar arrendatarios.

### Hito 3: Registro y Gestión de Propiedades para Arrendadores y Arrendatarios

Este hito incluye la implementación de un sistema de registro de usuarios, asignación de roles (arrendatario o arrendador) y la gestión de propiedades. Los arrendadores pueden publicar, editar y eliminar propiedades, mientras que los arrendatarios pueden ver las propiedades disponibles.

1. **Registro de Usuarios**
   - Se implementó un formulario personalizado de registro (`CustomUserCreationForm`) que incluye campos como `username`, `password`, `password_confirmation` y `rut`.
   - Se añadió un formulario adicional para seleccionar el tipo de usuario (`TipoUsuarioForm`), permitiendo elegir entre `Arrendatario` o `Arrendador`.
   - Los usuarios se registran correctamente y se asignan al grupo correspondiente (Arrendatario o Arrendador) según su elección.
   - Se implementó la redirección automática después del registro al inicio de sesión o a la página principal.

2. **Vistas de Registro y Login**
   - Se creó la vista de registro, donde los usuarios pueden registrarse y elegir su tipo (arrendatario o arrendador).
   - Se implementaron las vistas de inicio de sesión (`LoginView`) y cierre de sesión (`LogoutView`), junto con sus correspondientes templates HTML.
   - Se añadió redirección post-login a la página principal o a la vista de inicio de sesión.

3. **Gestión de Propiedades**
   - Se implementaron las vistas para la gestión de propiedades por parte de los arrendadores:
     - **Publicar Propiedad**: Los arrendadores pueden crear nuevas propiedades.
     - **Editar Propiedad**: Los arrendadores pueden editar las propiedades existentes.
     - **Eliminar Propiedad**: Los arrendadores pueden eliminar propiedades.
   - Se aseguraron de que solo los arrendadores puedan acceder a estas vistas mediante el uso de permisos (`@permission_required`).
   - Los arrendatarios tienen acceso a la vista para listar las propiedades disponibles.

4. **Grupos y Permisos**
   - Se crearon los grupos de usuarios `Arrendatario` y `Arrendador` en el panel de administración de Django.
   - Se asignaron permisos específicos a cada grupo:
     - **Arrendatario**: Permiso para listar propiedades y solicitar arrendamientos.
     - **Arrendador**: Permiso para publicar, editar, eliminar y listar propiedades.
   - Se asignan automáticamente a los usuarios registrados en el grupo correspondiente durante el proceso de registro.

5. **Verificación y Redirección**
   - Después de completar el registro, los usuarios son redirigidos a la página de inicio o a la vista de inicio de sesión.
   - Se verificó que los usuarios se registren correctamente en la base de datos y que se asignen a los grupos correspondientes, con los permisos adecuados.

6. **Próximos Pasos**
   - Implementar la lógica de aceptación de solicitudes de arrendatarios por parte de los arrendadores.
   - Mejorar las validaciones en los formularios y agregar mensajes de retroalimentación para el usuario.
   - Agregar pruebas unitarias para asegurar la integridad del sistema de registro y gestión de propiedades.


### Funcionalidades Implementadas en el Hito 4

1. Registro y Gestión de Usuarios
Los usuarios pueden registrarse como Arrendatario o Arrendador.
El registro incluye un formulario personalizado donde se asigna el tipo de usuario.
Los perfiles se crean automáticamente para cada usuario.
La asignación de grupos (Arrendatario o Arrendador) se realiza al momento de la creación del usuario.
2. Publicación de Propiedades (Inmuebles)
Los arrendadores pueden publicar propiedades mediante un formulario.
El formulario permite subir varias imágenes para cada propiedad y asociarlas al inmueble.
La vista de "Publicar Inmueble" tiene un diseño atractivo utilizando Bootstrap.
3. Visualización de Propiedades (Listar Inmuebles)
Los usuarios pueden ver una lista de propiedades con detalles como nombre, precio, y ubicación.
Las propiedades se muestran en un formato de cards en la página de inicio, con imágenes, nombre y precio.
El precio de los inmuebles se muestra en formato CLP (Pesos Chilenos).
4. Detalles de Propiedades
Al hacer clic en un inmueble desde la lista, se redirige al usuario a una página de detalles con una galería de imágenes (carrusel).
Se muestran las características del inmueble, como el precio mensual, la ubicación, el número de habitaciones, etc.
5. Carro de Imágenes
Las imágenes de cada propiedad pueden ser visualizadas en un carrusel responsivo en la página de detalles del inmueble.
6. Página Principal
En la página principal, se muestra un carrusel de imágenes de propiedades destacadas.
La página está organizada para mostrar las propiedades de manera atractiva, con diseño responsivo.


## Autor  
**Karen Limarí C.**
