from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .models import Ciudad
from .models import Usuario
from .models import CategoriaRestaurante

def login(request):
    usuarios = Usuario.objects.all()
    context = {'usuarios' : usuarios}
    return render(request, 'login.html', context)

def home(request):
    return render(request, 'home.html')

@login_required
def productos(request):
    return render(request, 'productos.html')

def exit(request):
    logout(request)
    return redirect('home')

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