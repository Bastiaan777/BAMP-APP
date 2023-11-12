from django.db import models

class Ciudad(models.Model):
    nombre = models.CharField(max_length=50)
    def __str__(self):
        return self.nombre

class CategoriaRestaurante(models.Model):
    idCategoriaRestaurante = models.CharField(max_length = 5)
    def __str__(self):
        return self.idCategoriaRestaurante
    nombreCategoriaRestaurante = models.CharField(max_length = 50)
    def __str__(self):
        return self.nombreCategoriaRestaurante

class Restaurante(models.Model):
    idRestaurante = models.CharField(max_length = 5)
    def __str__(self):
        return self.idRestaurante
    nombreRestaurante = models.CharField(max_length = 50)
    def __str__(self):
        return self.nombreRestaurante
    idCategoriaRestaurante = models.ForeignKey(CategoriaRestaurante, on_delete = models.CASCADE)
    def __str__(self):
        return self.idCategoriaRestaurante

class Carta(models.Model):
    idCarta = models.CharField(max_length = 5)
    def __str__(self):
        return self.idCarta
    numeroArticulos = models.IntegerField(default = 0)
    def __str__(self):
        return self.numeroArticulos
    idRestaurante = models.ForeignKey(Restaurante, on_delete = models.CASCADE)
    def __str__(self):
        return self.idRestaurante

class Producto(models.Model):
    idProducto = models.CharField(max_length = 5)
    def __str__(self):
        return self.idProducto
    nombreProducto = models.CharField(max_length = 50)
    def __str__(self):
        return self.nombreProducto
    descripcion = models.TextField(max_length = 600)
    def __str__(self):
        return self.descripcion
    precio = models.IntegerField()
    def __str__(self):
        return self.precio
    idCarta = models.ForeignKey(Carta, on_delete = models.CASCADE)
    def __str__(self):
        return self.idCarta

class Usuario(models.Model):
    idUsuario = models.CharField(max_length = 5)
    def __str__(self):
        return self.idUsuario
    nombreUsuario = models.CharField(max_length = 50)
    def __str__(self):
        return self.nombreUsuario
    apellidoUsuario = models.CharField(max_length = 50)
    def __str__(self):
        return self.apellidoUsuario
    fechaNacimiento = models.DateTimeField()
    def __str__(self):
        return self.fechaNacimiento
    direccion = models.TextField()
    def __str__(self):
        return self.direccion
    email = models.TextField()
    def __str__(self):
        return self.email
    nombreCiudad = models.ForeignKey(Ciudad, on_delete = models.CASCADE)
    def __str__(self):
        return self.nombreCiudad

class Pedido(models.Model):
    idPedido = models.CharField(max_length = 5)
    def __str__(self):
        return self.idPedido
    importePedido = models.IntegerField()
    def __str__(self):
        return self.importePedido
    idUsuario = models.ForeignKey(Usuario, on_delete = models.CASCADE)
    def __str__(self):
        return self.idUsuario

class CategoriaRestauranteCiudad(models.Model):
    nombreCiudad = models.ForeignKey(Ciudad, on_delete = models.CASCADE)
    def __str__(self):
        return self.nombreCiudad
    idCategoriaRestaurante = models.ForeignKey(CategoriaRestaurante, on_delete = models.CASCADE)
    def __str__(self):
        return self.idCategoriaRestaurante

class PedidoProducto(models.Model):
    idPedido = models.ForeignKey(Pedido, on_delete = models.CASCADE)
    def __str__(self):
        return self.idPedido
    idProducto = models.ForeignKey(Producto, on_delete = models.CASCADE)
    def __str__(self):
        return self.idProducto

