from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse
from django.contrib import messages
from .forms import AsociateForm
from .models import Usuario

# Create your views here.

def index(request):
    context = {
        'esta_logueado': True
    }
    return render(request, "core/index.html", context)

def lugares(request):
    return render(request, "core/lugares.html")

def socios(request):
    return render(request, "core/socios.html")

def usuario(request, nombre_usuario):
    context = {
        'nombre_usuario': 'Eugenia'
    }
    return render(request, "core/usuario.html", context)

def asociate(request):
    if request.method == "POST":
        formulario = AsociateForm(request.POST)

        if formulario.is_valid():
            messages.info(request, "Formulario enviado con éxito")

            u1 = Usuario(nombre="Primer", apellido="Usuario")
            u1.save()

            return redirect(reverse("index"))

    else:
        formulario = AsociateForm()

    context = {
        "asociate_form": formulario
    }
    return render(request, "core/asociate.html", context)

def lugar_detalle(request, id):
    return HttpResponse(f"Todo sobre el sitio N° {id}")