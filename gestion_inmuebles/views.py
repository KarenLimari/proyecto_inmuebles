from django.shortcuts import render, redirect
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import Group
from django.contrib.auth import update_session_auth_hash
from .forms import CustomUserCreationForm, TipoUsuarioForm
from .models import Perfil, Inmueble, ImagenInmueble
from .forms import (
    PerfilForm,
    CustomPasswordChangeForm,
    PublicarInmuebleForm, ImagenInmuebleForm
)  # Asegúrate de tener PerfilForm y CustomPasswordChangeForm





def home(request):
    inmuebles_destacados = Inmueble.objects.all()[:3]  # Selecciona los primeros 3 inmuebles
    return render(request, 'home.html', {'inmuebles_destacados': inmuebles_destacados})

def register(request):
    if request.method == "POST":
        user_form = CustomUserCreationForm(request.POST)
        tipo_usuario_form = TipoUsuarioForm(request.POST)

        if user_form.is_valid() and tipo_usuario_form.is_valid():
            user = user_form.save()
            tipo_usuario = tipo_usuario_form.cleaned_data["tipo_usuario"]
            user.tipo_usuario = tipo_usuario
            user.save()

            # Crear el perfil
            perfil = Perfil.objects.create(user=user)
            perfil.save()

            login(request, user)

            # Asignar al grupo según el tipo de usuario
            if tipo_usuario == "Arrendatario":
                group = Group.objects.get(name="Arrendatario")
                return redirect("perfil_usuario")  # Redirigir al perfil de arrendatario
            else:
                group = Group.objects.get(name="Arrendador")
                return redirect("publicar_inmueble")  # Redirigir al formulario de publicación de inmuebles

            user.groups.add(group)

        else:
            print(user_form.errors, tipo_usuario_form.errors)

    else:
        user_form = CustomUserCreationForm()
        tipo_usuario_form = TipoUsuarioForm()

    return render(request, "registration/register.html", {"user_form": user_form, "tipo_usuario_form": tipo_usuario_form})

class CustomLoginView(LoginView):
    template_name = "registration/login.html"


class CustomLogoutView(LogoutView):
    next_page = "/"


def choose_user_type(request):
    if request.method == "POST":
        form = TipoUsuarioForm(
            request.POST, instance=request.user
        )  # Vincula el formulario al usuario
        if form.is_valid():
            form.save()  # Guarda el tipo de usuario
            tipo_usuario = form.cleaned_data["tipo_usuario"]

            # Asignar el grupo según el tipo de usuario
            if tipo_usuario == "Arrendatario":
                group = Group.objects.get(name="Arrendatario")
            else:
                group = Group.objects.get(name="Arrendador")

            # Asignar al usuario el grupo correspondiente
            request.user.groups.add(group)

            return redirect("home")  # Redirige al home o a la página que desees
    else:
        form = TipoUsuarioForm(
            instance=request.user
        )  # Prefill el formulario con el usuario actual

    return render(request, "tipo_usuario.html", {"form": form})

@permission_required("gestion_inmuebles.add_inmueble", raise_exception=True)
@login_required
def publicar_inmueble(request):
    if request.method == "POST":
        form = PublicarInmuebleForm(request.POST, request.FILES)
        imagenes = request.FILES.getlist('imagenes')  # Captura múltiples imágenes
        if form.is_valid():
            inmueble = form.save(commit=False)
            inmueble.usuario = request.user  # Asocia el inmueble al usuario logueado
            inmueble.save()

            # Asocia las imágenes al inmueble
            for imagen in imagenes:
                ImagenInmueble.objects.create(inmueble=inmueble, imagen=imagen)

            return redirect("listar_propiedades")  # Redirige a la lista de propiedades
    else:
        form = PublicarInmuebleForm()

    return render(request, "publicar_inmueble.html", {"form": form})


# Vista para que el arrendatario vea las propiedades disponibles
@login_required
def listar_propiedades(request):
    inmuebles = Inmueble.objects.prefetch_related("imagenes").all()  # Recupera inmuebles con sus imágenes
    return render(request, "listar_propiedades.html", {"inmuebles": inmuebles})


# Vista para que el arrendador pueda editar la propiedad
@permission_required("gestion_inmuebles.change_inmueble", raise_exception=True)
@login_required
def editar_propiedad(request, inmueble_id):
    inmueble = Inmueble.objects.get(id=inmueble_id)
    if request.method == "POST":
        # Lógica para editar la propiedad
        # ...
        return redirect("home")
    return render(request, "editar_propiedad.html", {"inmueble": inmueble})


# Vista para que el arrendador elimine una propiedad
@permission_required("gestion_inmuebles.delete_inmueble", raise_exception=True)
@login_required
def eliminar_propiedad(request, inmueble_id):
    inmueble = Inmueble.objects.get(id=inmueble_id)
    if request.method == "POST":
        inmueble.delete()
        return redirect("home")
    return render(request, "eliminar_propiedad.html", {"inmueble": inmueble})


@login_required
def editar_perfil(request):
    try:
        perfil = Perfil.objects.get(user=request.user)
    except Perfil.DoesNotExist:
        perfil = Perfil.objects.create(user=request.user)

    if request.method == "POST":
        form = PerfilForm(request.POST, instance=perfil)
        if form.is_valid():
            form.save()
            return redirect("perfil_usuario")  # Redirige al perfil después de editarlo
    else:
        form = PerfilForm(instance=perfil)

    return render(request, "editar_perfil.html", {"form": form})


# Vista para cambiar la contraseña del usuario
@login_required
def cambiar_contraseña(request):
    if request.method == "POST":
        form = CustomPasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)  # Mantiene la sesión activa después del cambio
            return redirect("perfil_usuario")
    else:
        form = CustomPasswordChangeForm(request.user)

    return render(request, "cambiar_contraseña.html", {"form": form})


@login_required
def perfil_usuario(request):
    return render(request, "perfil_usuario.html", {"usuario": request.user})

@login_required
def detalle_inmueble(request, slug):
    inmueble = Inmueble.objects.prefetch_related("imagenes").get(slug=slug)
    return render(request, "detalle_inmueble.html", {"inmueble": inmueble})

