from django.contrib import admin
from .models import Ciudad, CategoriaRestaurante, Restaurante, Producto, Pedido, PerfilUsuario, PedidoProducto

admin.site.register(Ciudad)
admin.site.register(CategoriaRestaurante)
admin.site.register(Producto)
admin.site.register(Pedido)
admin.site.register(PerfilUsuario)
admin.site.register(PedidoProducto)

class RestauranteAdmin(admin.ModelAdmin):
    list_display = ('nombreRestaurante', 'categoriaRestaurante')  # Campos que quieres mostrar
    list_filter = ('categoriaRestaurante',)  # Aquí agregas el campo por el cual filtrar
    ordering = ['categoriaRestaurante']
    
admin.site.register(Restaurante, RestauranteAdmin)