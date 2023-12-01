from django.db import models

class Ciudad(models.Model):
    nombre = models.CharField(max_length=50)
    
    def __str__(self):
        return self.nombre

class CategoriaRestaurante(models.Model):
    nombreCategoriaRestaurante = models.CharField(max_length = 50)
    imagen= models.ImageField(upload_to='imagenes_categoria_restaurante', height_field=None, width_field=None, max_length=100)
    ciudades = models.ManyToManyField(Ciudad)

    def __str__(self):
        return self.nombreCategoriaRestaurante

class Restaurante(models.Model):
    nombreRestaurante = models.CharField(max_length = 50)
    categoriaRestaurante = models.ForeignKey(CategoriaRestaurante, on_delete = models.CASCADE)

    def __str__(self):
        return self.nombreRestaurante
    
   
"""
class Carta(models.Model):
    numeroArticulos = models.IntegerField(default = 0)
    restaurante = models.ForeignKey(Restaurante, on_delete = models.CASCADE)

    def __str__(self):
        return self.id
 """
    
    

class Producto(models.Model):
    descripcion = models.TextField(max_length = 600)
    precio = models.IntegerField()
    nombreProducto = models.CharField(max_length = 50)
    restaurante = models.ForeignKey(Restaurante, on_delete = models.CASCADE)
    def __str__(self):
        return self.nombreProducto
    
    

class Usuario(models.Model):
    nombreUsuario = models.CharField(max_length = 50)
    apellidoUsuario = models.CharField(max_length = 50)
    fechaNacimiento = models.DateTimeField()
    direccion = models.TextField()
    email = models.TextField()
    ciudad = models.ForeignKey(Ciudad, on_delete = models.CASCADE)
    def __str__(self):
        return self.nombreUsuario
    

class Pedido(models.Model):
    importePedido = models.IntegerField()
    usuario = models.ForeignKey(Usuario, on_delete = models.CASCADE)
    productos = models.ManyToManyField(Producto)
    def __str__(self):
        return self.idPedido
    
    
"""
CREEMOS QUE ESTO NO HACE FALTA Y LO PODREMOS BORRAR
class PedidoProducto(models.Model):
    idPedido = models.ForeignKey(Pedido, on_delete = models.CASCADE)
    idProducto = models.ForeignKey(Producto, on_delete = models.CASCADE)
"""
    

 