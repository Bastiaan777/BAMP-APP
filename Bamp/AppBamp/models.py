from django.db import models

class Ciudad(models.Model):
    nombre = models.Charfield(max_length=50)

class CategoriaRestaurante(models.Model):
    idCategoriaRestaurante = models.Charfield(max_length = 5)
    nombreCategoriaRestaurante = models.Charfield(max_length = 50)

class Restaurante(models.Model):
    idRestaurante = models.Charfield(max_length = 5)
    nombreRestaurante = models.Charfield(max_length = 50)
    idCategoriaRestaurante = models.ForeignKey(CategoriaRestaurante, on_delete = models.CASCADE)

class Carta(models.Model):
    idCarta = models.Charfield(max_length = 5)
    numeroArticulos = models.integerField(default = 0)
    idRestaurante = models.ForeignKey(Restaurante, on_delete = models.CASCADE)

class Producto(models.Model):
    idProducto = models.Charfield(max_length = 5)
    nombreProducto = models.Charfield(max_length = 50)
    descripcion = models.Textfield(max_length = 600)
    precio = models.integerField()
    idCarta = models.ForeignKey(Carta, on_delete = models.CASCADE)

class Usuario(models.Model):
    idUsuario = models.Charfield(max_length = 5)
    nombreUsuario = models.Charfield(max_length = 50)
    apellidoUsuario = models.Charfield(max_length = 50)
    fechaNacimiento = models.DateTimeField()
    direccion = models.Textfield()
    email = models.Textfield()
    nombreCiudad = models.ForeignKey(Ciudad, on_delete = models.CASCADE)

class Pedido(models.Model):
    idPedido = models.Charfield(max_length = 5)
    importePedido = models.integerField()
    idUsuario = models.ForeignKey(Usuario, on_delete = models.CASCADE)

class CategoriaRestauranteCiudad(models.Model):
    nombreCiudad = models.ForeignKey(Ciudad, on_delete = model.CASCADE)
    idCategoriaRestaurante = models.ForeignKey(CategoriaRestaurante, on_delete = model.CASCADE)

class PedidoProducto(models.Model):
    idPedido = models.ForeignKey(Pedido, on_delete = model.CASCADE)
    idProducto = models.ForeignKey(Producto, on_delete = model.CASCADE)

