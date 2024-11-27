# gestion_inmuebles/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('registro/', views.registro, name='registro'),  # Ruta para el registro
    path('', views.home, name='home'),  # Página principal (si la tienes)
]