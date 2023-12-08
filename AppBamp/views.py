from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.http import require_POST 
from django.contrib.auth.models import User
from .forms import PerfilUsuarioForm, ExtendedUserCreationForm


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

def politica(request):
    return render(request, 'politicaprivacidad.html')
   

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
    print(request.user)
    user = User.objects.get(username=request.user)
    perfil = PerfilUsuario.objects.get(usuario=user)
    return render(request, 'perfil.html', { "perfil": perfil })


def registro(request):
    if request.method == 'POST':
        print("es un post")
        user_form = ExtendedUserCreationForm(request.POST)
        perfil_usuario_form = PerfilUsuarioForm(request.POST)
        print("Se han creado los formularios")
        print(f"USER FORM IS VALID {user_form.is_valid()}")
        print(f"PERFIL FORM IS VALID {perfil_usuario_form.is_valid()}")
        if user_form.is_valid() and perfil_usuario_form.is_valid():
            print("los formularios son validos")
            user = user_form.save()
            perfil_usuario = perfil_usuario_form.save(commit=False) 
            perfil_usuario.usuario = user
            perfil_usuario.save()
            return redirect('home')
        else:
            print(user_form.errors)
            print(perfil_usuario_form.errors)
    else:
        user_form = ExtendedUserCreationForm()
        perfil_usuario_form = PerfilUsuarioForm()

    return render(request, 'registration/registro.html', {'user_form': user_form, 'perfil_usuario_form': perfil_usuario_form})



@require_POST #la view es la que interactua con la base de datos
def categoria_restaurante(request):

    # Retrieve the data from the form submission
    id_ciudad = request.POST.get('id_ciudad') #linea 18 del ciudades.html, es el mismo id_ciudad
    ciudad = Ciudad.objects.get(pk=id_ciudad) #SELECT * FROM AppBamp_ciudad WHERE id=1; --> esto es lo que esta haciendo 
    categorias = CategoriaRestaurante.objects.filter(restaurante__ciudad=ciudad).distinct()
    contexto = {'categorias': categorias} 
    return render(request, 'categorias_restaurante.html', contexto)


@require_POST
def restaurantes(request):
    id_categoria = request.POST.get('id-categoria')
    restaurantes = Restaurante.objects.filter(categoriaRestaurante_id=id_categoria)
    contexto = {'restaurantes': restaurantes}
    return render(request, 'restaurantes.html', contexto)


@require_POST
def carta(request):
    id_restaurante = request.POST.get('id-restaurante')
    lista_productos = Producto.objects.filter(restaurante_id=id_restaurante) #filter -> Esperas mas de un resultado en la query
    print(lista_productos)
    contexto = {'carta':lista_productos}
    return render(request, 'carta.html', contexto)

@require_POST
def pedido(request):
    if request.user.is_authenticated:
        print(request.user)
        pedido = Pedido()
        usuario = User.objects.get(username=request.user) #cargamos el objeto User con el username
        perfil_usuario = PerfilUsuario.objects.get(usuario=usuario) #get es algo unico
        pedido.usuario = perfil_usuario
        pedido.save()
        for nombre_variable, cantidad in request.POST.items():
            if nombre_variable.startswith('cantidad_'):
                id_producto = nombre_variable.split('_')[1]
                producto = Producto.objects.get(pk=id_producto)
                
                if cantidad and int(cantidad) > 0:
                    pedido_producto = PedidoProducto()
                    pedido_producto.producto = producto
                    pedido_producto.pedido = pedido
                    pedido_producto.cantidad = int(cantidad)
                    pedido_producto.save()
                    pedido.importePedido += producto.precio * int(cantidad)
        pedido.save()
        return render(request, 'informePedido.html') 
    else:
        return HttpResponse('Usuario no autenticado')


def informePedido(request):
    return render(request, 'informePedido.html')