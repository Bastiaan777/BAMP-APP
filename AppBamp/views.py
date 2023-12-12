from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse, HttpResponseBadRequest
from django.views.decorators.http import require_POST 
from django.contrib.auth.models import User
from .forms import PerfilUsuarioForm, ExtendedUserCreationForm
from .models import Producto

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

def verificar_usuario(request):
    username = request.GET.get('username')
    if username is not None:
        # Buscar el user en la BD
        usuario_existe = User.objects.filter(username=username).exists()
        data = {
            "usuarioExiste": usuario_existe
        }
        return JsonResponse(data)
    else:
        return HttpResponseBadRequest("Paramtero obligatorio 'username' no introducido")




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
    return redirect('login')

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
    pedidos = Pedido.objects.filter(usuario=perfil).order_by('-id')
    contexto = { 
        "perfil": perfil,
        "pedidos" : pedidos
    }
    return render(request, 'perfil.html', contexto)



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

   
    id_ciudad = request.POST.get('id_ciudad') 
    ciudad = Ciudad.objects.get(pk=id_ciudad) 
    categorias = CategoriaRestaurante.objects.filter(restaurante__ciudad=ciudad).distinct()
    contexto = {'categorias': categorias, 'ciudad' : ciudad} 
    return render(request, 'categorias_restaurante.html', contexto)


@require_POST
def restaurantes(request):
    id_categoria = request.POST.get('id-categoria')
    id_ciudad = request.POST.get('id-ciudad')
    ciudad = Ciudad.objects.get(pk=id_ciudad)
    id_ciudad = request.POST.get('id-ciudad')
    ciudad = Ciudad.objects.get(pk=id_ciudad)
    restaurantes = Restaurante.objects.filter(categoriaRestaurante_id=id_categoria, ciudad=ciudad)
    contexto = {'restaurantes': restaurantes}
    return render(request, 'restaurantes.html', contexto)


@require_POST
def carta(request):
    id_restaurante = request.POST.get('id-restaurante')
    lista_productos = Producto.objects.filter(restaurantes=id_restaurante).order_by('nombreProducto')
    print(lista_productos)
    contexto = {'carta': lista_productos}
    return render(request, 'carta.html', contexto)

@require_POST
def pedido(request):
    if request.user.is_authenticated:
        print(request.user)
        pedido = Pedido()
        usuario = User.objects.get(username=request.user) 
        perfil_usuario = PerfilUsuario.objects.get(usuario=usuario) 
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
        return redirect(f'/informe-pedido?id={pedido.id}')
    else:
        return HttpResponse('Usuario no autenticado')


def resumen_pedido(request):
    id_pedido = request.GET.get('id')
    pedido = Pedido.objects.get(pk=id_pedido)
    productos_pedido = PedidoProducto.objects.filter(pedido=pedido)

    productos = []
    for producto_pedido in productos_pedido:
        productos.append({
            'nombre': producto_pedido.producto.nombreProducto,
            'descripcion': producto_pedido.producto.descripcion,
            'precio': producto_pedido.producto.precio * producto_pedido.cantidad,
            'cantidad': producto_pedido.cantidad
        })

    contexto = {
        'pedido': pedido,
        'productos': productos,
    }
    return render(request, 'resumenPedido.html', contexto) 
