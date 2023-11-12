from django.http import HttpResponse
from django.shortcuts import render
from .models import Ciudad
from .models import CategoriaRestaurante

def index(request):
    return HttpResponse("hola")

def ciudades(request):

    ciudades= Ciudad.objects.all()
    context = {'ciudades' : ciudades}
    return render(request, 'ciudades.html', context)

def categoria_restaurante(request):
    categorias= CategoriaRestaurante.objects.all()
    context = {'categorias' : categorias}
    return render(request, 'categorias_restaurante.html', context)
    