from django.contrib import admin
from .models import Ciudad, CategoriaRestaurante, Restaurante, Producto, Pedido, PerfilUsuario

admin.site.register(Ciudad)
admin.site.register(CategoriaRestaurante)
admin.site.register(Restaurante)
admin.site.register(Producto)
admin.site.register(Pedido)
admin.site.register(PerfilUsuario)
