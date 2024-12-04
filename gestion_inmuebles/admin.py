from django.contrib import admin
from .models import User, Inmueble, TipoInmueble, Region, Comuna, ImagenInmueble

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'tipo_usuario', 'rut')
    search_fields = ('username', 'email', 'tipo_usuario', 'rut')

@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
    search_fields = ('nombre',)

@admin.register(Comuna)
class ComunaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'region')
    search_fields = ('nombre',)
    list_filter = ('region',)

@admin.register(TipoInmueble)
class TipoInmuebleAdmin(admin.ModelAdmin):
    list_display = ('tipo',)

@admin.register(Inmueble)
class InmuebleAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion', 'precio_mensual', 'region', 'comuna', 'tipo_inmueble', 'slug', 'mostrar_imagenes')
    search_fields = ('nombre', 'descripcion')
    list_filter = ('comuna', 'tipo_inmueble')

    # Función para mostrar las imágenes en list_display
    def mostrar_imagenes(self, obj):
        imagenes = obj.imagenes.all()  # Obtiene todas las imágenes asociadas al inmueble
        # Devuelve un string con las URLs de las imágenes o las visualiza
        return ", ".join([f'<img src="{imagen.imagen.url}" style="width:50px;height:50px;" />' for imagen in imagenes])
    mostrar_imagenes.allow_tags = True  # Habilita el renderizado de HTML (las imágenes)
    mostrar_imagenes.short_description = 'Imágenes'
    
@admin.register(ImagenInmueble)
class ImagenInmuebleAdmin(admin.ModelAdmin):
    list_display = ('inmueble', 'imagen', 'imagen_url')
    search_fields = ('inmueble__nombre',)  # Para poder buscar por el nombre del inmueble