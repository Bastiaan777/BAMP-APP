from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth import authenticate, login, logout
from .models import Ciudad
from django.http import HttpResponse, HttpResponseRedirect
from .models import Usuario
from .models import CategoriaRestaurante
from django.views.decorators.http import require_POST 

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        try:
            user = authenticate(request, username = username, password = password)
        except Exception as e:
            return HttpResponse(e)
        if(user is not None):
            login(request, user)
            return render(request, 'home.html')
        else:
            return HttpResponse('Usuario no creado')
 
    return render(request, 'registration/login.html')

def home(request):
    if(request.user.is_authenticated):
        return render(request, 'home.html')
    else:
        return render(request, 'registration/login.html')
        #alert

@login_required
def productos(request):
    return render(request, 'productos.html')

def exit(request):
    logout(request)
    return render(request, 'registration/login.html')

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