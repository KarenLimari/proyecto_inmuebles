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

class ImagenInmuebleInline(admin.TabularInline):  # O usa StackedInline si prefieres el diseño vertical
    model = ImagenInmueble
    extra = 1  # Esto añade un formulario adicional vacío para añadir más imágenes
    fields = ['imagen', 'imagen_url']  # Los campos que deseas mostrar en el inline

@admin.register(Inmueble)
class InmuebleAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion', 'precio_mensual', 'region', 'comuna', 'tipo_inmueble', 'slug', 'mostrar_imagenes')
    search_fields = ('nombre', 'descripcion')
    list_filter = ('comuna', 'tipo_inmueble')
    inlines = [ImagenInmuebleInline]  # Asegúrate de agregar esto para que puedas ver y agregar imágenes desde el admin

    def mostrar_imagenes(self, obj):
        imagenes = obj.imagenes.all()  # Obtiene todas las imágenes asociadas al inmueble
        return ", ".join([f'<img src="{imagen.imagen.url}" style="width:50px;height:50px;" />' for imagen in imagenes])
    mostrar_imagenes.allow_tags = True  # Permite el renderizado de HTML
    mostrar_imagenes.short_description = 'Imágenes'

# Si también quieres poder gestionar las imágenes de forma separada:
@admin.register(ImagenInmueble)
class ImagenInmuebleAdmin(admin.ModelAdmin):
    list_display = ('inmueble', 'imagen', 'imagen_url')
    search_fields = ('inmueble__nombre',) 