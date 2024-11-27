# gestion_inmuebles/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

def home(request):
    return render(request, 'home.html')  # Renderiza el template home.html

def registro(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()  # Guarda el nuevo usuario
            messages.success(request, "¡Registro exitoso! Ya puedes iniciar sesión.")
            return redirect('login')  # Redirige al login después del registro
        else:
            messages.error(request, "Hubo un error en el formulario. Por favor intenta de nuevo.")
    else:
        form = UserCreationForm()

    return render(request, 'registro.html', {'form': form})