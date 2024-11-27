from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import Group
from .forms import TipoUsuarioForm  # Importar el formulario
from .models import Inmueble # Importar el formulario

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

            # Asignar el grupo según el tipo de usuario
            if tipo_usuario == 'Arrendatario':
                group = Group.objects.get(name='Arrendatario')
            else:
                group = Group.objects.get(name='Arrendador')
            
            # Asignar al usuario el grupo correspondiente
            user.groups.add(group)

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
            tipo_usuario = form.cleaned_data['tipo_usuario']

            # Asignar el grupo según el tipo de usuario
            if tipo_usuario == 'Arrendatario':
                group = Group.objects.get(name='Arrendatario')
            else:
                group = Group.objects.get(name='Arrendador')
            
            # Asignar al usuario el grupo correspondiente
            request.user.groups.add(group)

            return redirect('home')  # Redirige al home o a la página que desees
    else:
        form = TipoUsuarioForm(instance=request.user)  # Prefill el formulario con el usuario actual

    return render(request, 'tipo_usuario.html', {'form': form})

# Vista para que el arrendador pueda publicar propiedades
@permission_required('gestion_inmuebles.add_inmueble', raise_exception=True)
@login_required
def publicar_propiedad(request):
    if request.method == 'POST':
        # Lógica para crear una nueva propiedad
        # ...
        return redirect('home')  # Redirige a la página de inicio
    return render(request, 'publicar_propiedad.html')  # Formulario para crear propiedad

# Vista para que el arrendatario vea las propiedades disponibles
@login_required
def listar_propiedades(request):
    inmuebles = Inmueble.objects.all()  # Filtrar si es necesario
    return render(request, 'listar_propiedades.html', {'inmuebles': inmuebles})

# Vista para que el arrendador pueda editar la propiedad
@permission_required('gestion_inmuebles.change_inmueble', raise_exception=True)
@login_required
def editar_propiedad(request, inmueble_id):
    inmueble = Inmueble.objects.get(id=inmueble_id)
    if request.method == 'POST':
        # Lógica para editar la propiedad
        # ...
        return redirect('home')
    return render(request, 'editar_propiedad.html', {'inmueble': inmueble})

# Vista para que el arrendador elimine una propiedad
@permission_required('gestion_inmuebles.delete_inmueble', raise_exception=True)
@login_required
def eliminar_propiedad(request, inmueble_id):
    inmueble = Inmueble.objects.get(id=inmueble_id)
    if request.method == 'POST':
        inmueble.delete()
        return redirect('home')
    return render(request, 'eliminar_propiedad.html', {'inmueble': inmueble})