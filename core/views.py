from django.shortcuts import render
from django.http import HttpResponse

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

def lugar_detalle(request, id):
    return HttpResponse(f"Todo sobre el sitio N° {id}")