# gestion_inmuebles/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import login
from .forms import TipoUsuarioForm  # Importar el formulario

def home(request):
    return render(request, 'home.html')  # Renderiza el template home.html
def register(request):
    if request.method == 'POST':
        user_form = UserCreationForm(request.POST)
        tipo_usuario_form = TipoUsuarioForm(request.POST)
        
        if user_form.is_valid() and tipo_usuario_form.is_valid():
            # Guarda el usuario
            user = user_form.save()
            # Asigna el tipo de usuario
            tipo_usuario = tipo_usuario_form.cleaned_data['tipo_usuario']
            user.tipo_usuario = tipo_usuario  # Establece el tipo de usuario en el modelo
            user.save()  # Guarda el usuario con el tipo de usuario

            login(request, user)

            return redirect('home')  # Redirige a la página de inicio o a la página que desees

    else:
        user_form = UserCreationForm()
        tipo_usuario_form = TipoUsuarioForm()

    return render(request, 'registration/register.html', {'user_form': user_form, 'tipo_usuario_form': tipo_usuario_form})

class CustomLoginView(LoginView):
    template_name = 'registration/login.html'

class CustomLogoutView(LogoutView):
    next_page = '/' 

def choose_user_type(request):
    if request.method == 'POST':
        form = TipoUsuarioForm(request.POST, instance=request.user)  # Vincula el formulario al usuario
        if form.is_valid():
            form.save()  # Guarda el tipo de usuario
            return redirect('home')  # Redirige al home o a la página que desees
    else:
        form = TipoUsuarioForm(instance=request.user)  # Prefill el formulario con el usuario actual

    return render(request, 'tipo_usuario.html', {'form': form})