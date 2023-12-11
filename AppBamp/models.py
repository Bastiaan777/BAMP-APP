from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User


class PerfilUsuario(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE) #usuario es un objeto
    fechaNacimiento = models.DateField(blank=True, null=True) #puede estar vacio
    direccion = models.TextField(blank=True, null=True)
    def __str__(self):
        return self.usuario.username


class Ciudad(models.Model):
    nombre = models.CharField(max_length=50)
    
    def __str__(self):
        return self.nombre

class CategoriaRestaurante(models.Model):
    nombreCategoriaRestaurante = models.CharField(max_length = 50)
    imagen= models.ImageField(upload_to='imagenes_categoria_restaurante', height_field=None, width_field=None, max_length=100)

    def __str__(self):
        return self.nombreCategoriaRestaurante

class Restaurante(models.Model):
    nombreRestaurante = models.CharField(max_length = 50)
    ciudad = models.ForeignKey(Ciudad, on_delete=models.CASCADE)
    categoriaRestaurante = models.ForeignKey(CategoriaRestaurante, on_delete = models.CASCADE)
    descripcion = models.CharField(max_length = 255, default="Sin descripción")
    hAperturaRestaurante = models.TimeField(null = True, blank = True)
    hCierreRestaurante = models.TimeField(null = True, blank = True)
    direccion = models.CharField(max_length = 255, default="Sin dirección establecida")
    telefono = models.CharField(max_length = 255, default="Sin teléfono")
    imagen = models.ImageField(upload_to="restaurantes/imagenes/", default="sin_imagen.png")

    def __str__(self):
        return self.nombreRestaurante


class Producto(models.Model):
    descripcion = models.TextField(max_length=600)
    precio = models.DecimalField(max_digits=6, decimal_places=2)
    nombreProducto = models.CharField(max_length=50)
    restaurante = models.ManyToManyField(Restaurante)
    def __str__(self):
        return self.nombreProducto
    

class Pedido(models.Model):
    importePedido = models.IntegerField(default=0)
    usuario = models.ForeignKey(PerfilUsuario, on_delete=models.CASCADE)
    productos = models.ManyToManyField(Producto, through="PedidoProducto")
    def __str__(self):
        return f"id: {self.id}"


class PedidoProducto(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField()

    class Meta:
        unique_together = ("pedido", "producto")
    
    def __str__(self):
        return f"pedido: {self.pedido.id} - producto: {self.producto.id} - cantidad: {self.cantidad}"