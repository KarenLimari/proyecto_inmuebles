from django.contrib import admin
from .models import Inmueble, TipoInmueble, Region, Comuna

class InmuebleAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion', 'tipo_inmueble', 'precio_mensual', 'comuna')
    search_fields = ('nombre', 'descripcion', 'comuna')
    list_filter = ('tipo_inmueble', 'comuna')

class TipoInmuebleAdmin(admin.ModelAdmin):
    list_display = ('tipo',)
    search_fields = ('tipo',)

class RegionAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
    search_fields = ('nombre',)

class ComunaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'region')
    search_fields = ('nombre',)
    list_filter = ('region',)

# Registrar los modelos con sus clases personalizadas
admin.site.register(Inmueble, InmuebleAdmin)
admin.site.register(TipoInmueble, TipoInmuebleAdmin)
admin.site.register(Region, RegionAdmin)
admin.site.register(Comuna, ComunaAdmin)
