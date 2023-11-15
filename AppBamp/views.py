from django.shortcuts import render
from .models import Ciudad
from .models import CategoriaRestaurante

def ciudades(request):
    ciudades = Ciudad.objects.all()
    context = {'ciudades': ciudades}
    return render(request, 'ciudades.html', context)

def categoria_restaurante(request):
    categorias = Ciudad.objects.all()
    context = {'categorias': categorias}
    return render(request, 'categorias_restaurante.html', context)


# def categoria_restaurante(request, ciudad):
#     categorias = Ciudad.objects.get(id=ciudad).categorias_restaurante.all()
#     context = {'categorias': categorias}
#     return render(request, 'categorias_restaurante.html', context)