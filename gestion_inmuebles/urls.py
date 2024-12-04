# gestion_inmuebles/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),  # Ruta para el registro
    path('', views.home, name='home'),
    path('perfil/editar/', views.editar_perfil, name='editar_perfil'),
    path('cambiar_contraseña/', views.cambiar_contraseña, name='cambiar_contraseña'),
    path('perfil/', views.perfil_usuario, name='perfil_usuario'),
    path('listar_propiedades/', views.listar_propiedades, name='listar_propiedades'),  # Listar propiedades
    path('publicar_inmueble/', views.publicar_inmueble, name='publicar_inmueble'),
    path('inmueble/<slug:slug>/', views.detalle_inmueble, name='detalle_inmueble'),
    path('inmuebles/', views.listar_propiedades, name='listar_propiedades'),  # Listado de inmuebles
    path('inmueble/<int:inmueble_id>/', views.detalle_inmueble, name='detalle_inmueble'),  # Detalles de inmueble
]
