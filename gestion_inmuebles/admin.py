from django.contrib import admin
from .models import User, Inmueble, TipoInmueble, Region, Comuna

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
    list_display = ('nombre', 'comuna', 'precio_mensual', 'usuario')
    search_fields = ('nombre', 'comuna__nombre', 'usuario__username')
    list_filter = ('comuna', 'tipo_inmueble', 'usuario')
