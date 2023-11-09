from django.db import models

class Ciudad(models.Model):
    nombre = models.CharField(max_length=50)

class CategoriaRestaurante(models.Model):
    idCategoriaRestaurante = models.CharField(max_length = 5)
    nombreCategoriaRestaurante = models.CharField(max_length = 50)

class Restaurante(models.Model):
    idRestaurante = models.CharField(max_length = 5)
    nombreRestaurante = models.CharField(max_length = 50)
    idCategoriaRestaurante = models.ForeignKey(CategoriaRestaurante, on_delete = models.CASCADE)

class Carta(models.Model):
    idCarta = models.CharField(max_length = 5)
    numeroArticulos = models.IntegerField(default = 0)
    idRestaurante = models.ForeignKey(Restaurante, on_delete = models.CASCADE)

class Producto(models.Model):
    idProducto = models.CharField(max_length = 5)
    nombreProducto = models.CharField(max_length = 50)
    descripcion = models.TextField(max_length = 600)
    precio = models.IntegerField()
    idCarta = models.ForeignKey(Carta, on_delete = models.CASCADE)

class Usuario(models.Model):
    idUsuario = models.CharField(max_length = 5)
    nombreUsuario = models.CharField(max_length = 50)
    apellidoUsuario = models.CharField(max_length = 50)
    fechaNacimiento = models.DateTimeField()
    direccion = models.TextField()
    email = models.TextField()
    nombreCiudad = models.ForeignKey(Ciudad, on_delete = models.CASCADE)

class Pedido(models.Model):
    idPedido = models.CharField(max_length = 5)
    importePedido = models.IntegerField()
    idUsuario = models.ForeignKey(Usuario, on_delete = models.CASCADE)

class CategoriaRestauranteCiudad(models.Model):
    nombreCiudad = models.ForeignKey(Ciudad, on_delete = models.CASCADE)
    idCategoriaRestaurante = models.ForeignKey(CategoriaRestaurante, on_delete = model.CASCADE)

class PedidoProducto(models.Model):
    idPedido = models.ForeignKey(Pedido, on_delete = models.CASCADE)
    idProducto = models.ForeignKey(Producto, on_delete = model.CASCADE)

