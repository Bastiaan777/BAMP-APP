from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .models import Ciudad
from .models import Usuario
from .models import CategoriaRestaurante
from django.views.decorators.http import require_POST 

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

@require_POST #la view es la que interactua con la base de datos
def categoria_restaurante(request):
    # Retrieve the data from the form submission
    id_ciudad = request.POST.get('id_ciudad') #linea 18 del ciudades.html, es el mismo id_ciudad
    ciudad = Ciudad.objects.get(pk=id_ciudad) #SELECT * FROM AppBamp_ciudad WHERE id=1; --> esto es lo que esta haciendo 
    categorias = CategoriaRestaurante.objects.filter(ciudades=ciudad) #ya tenemos las categorias de la ciudad seleccionada
    contexto = {'categorias': categorias} 
    return render(request, 'categorias_restaurante.html', contexto)
    


# def categoria_restaurante(request, ciudad):
#     categorias = Ciudad.objects.get(id=ciudad).categorias_restaurante.all()
#     context = {'categorias': categorias}
#     return render(request, 'categorias_restaurante.html', context)