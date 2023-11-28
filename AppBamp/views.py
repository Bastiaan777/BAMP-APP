from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.http import require_POST 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import * 


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
    if(request.user.is_authenticated):
        ciudades = Ciudad.objects.all()
        context = {'ciudades': ciudades}
        return render(request, 'ciudades.html', context)
    else:
        return render(request, 'registration/login.html')
        #alert
def perfil(request):
    return render(request, 'perfil.html')


def registro(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'registration/registro.html', {'form': form})



@require_POST #la view es la que interactua con la base de datos
def categoria_restaurante(request):

    # Retrieve the data from the form submission
    id_ciudad = request.POST.get('id_ciudad') #linea 18 del ciudades.html, es el mismo id_ciudad
    ciudad = Ciudad.objects.get(pk=id_ciudad) #SELECT * FROM AppBamp_ciudad WHERE id=1; --> esto es lo que esta haciendo 
    categorias = CategoriaRestaurante.objects.filter(ciudades=ciudad) #ya tenemos las categorias de la ciudad seleccionada
    contexto = {'categorias': categorias} 
    return render(request, 'categorias_restaurante.html', contexto)


@require_POST
def restaurantes(request):
    id_categoria = request.POST.get('id-categoria')
    print(id_categoria)
    restaurantes = Restaurante.objects.filter(categoriaRestaurante_id=id_categoria)
    contexto = {'restaurantes': restaurantes}
    print(contexto)
    return render(request, 'restaurantes.html', contexto)

    

    


# def categoria_restaurante(request, ciudad):
#     categorias = Ciudad.objects.get(id=ciudad).categorias_restaurante.all()
#     context = {'categorias': categorias}
#     return render(request, 'categorias_restaurante.html', context)