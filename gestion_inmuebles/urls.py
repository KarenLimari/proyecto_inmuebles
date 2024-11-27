# gestion_inmuebles/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),  # Ruta para el registro
    path('', views.home, name='home'),  # Página principal (si la tienes)
]