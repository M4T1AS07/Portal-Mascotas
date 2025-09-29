from django.shortcuts import render, get_object_or_404
from .models import Mascota, Post
from .forms import SolicitudAdopcionForm


def lista_mascotas(request):
    mascotas = Mascota.objects.filter(disponible=True, solicitudadopcion=False)

    especie = request.GET.get("especie")
    edad = request.GET.get("edad")
    ubicacion = request.GET.get("ubicacion")

    if especie:
        mascotas = mascotas.filter(especie__iexact=especie)
    if edad:
        mascotas = mascotas.filter(edad=edad)
    if ubicacion and hasattr(Mascota, "ubicacion"):
        mascotas = mascotas.filter(ubicacion__icontains=ubicacion)

    return render(request, 'portal/mascota.html', {'mascotas': mascotas})


from django.contrib import messages
from django.shortcuts import redirect

def solicitar_adopcion(request, mascota_id):
    mascota = get_object_or_404(Mascota, id=mascota_id)
    if request.method == "POST":
        form = SolicitudAdopcionForm(request.POST)
        if form.is_valid():
            solicitud = form.save(commit=False)
            solicitud.mascota = mascota
            solicitud.save()
            messages.success(request, f"Tu solicitud para adoptar a {mascota.nombre} fue enviada con éxito.")
            return redirect("home")
    else:
        form = SolicitudAdopcionForm()

    return render(request, "portal/solicitudadopcion.html", {"form": form, "mascota": mascota})



def blog(request):
    entradas = Post.objects.all().order_by("-fecha")
    return render(request, "portal/post.html", {"entradas": entradas})

def home(request):
    mascotas_disponibles = Mascota.objects.filter(solicitudadopcion=False)
    return render(request, 'portal/home.html', {'mascotas': mascotas_disponibles})