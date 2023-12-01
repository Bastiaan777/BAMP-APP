from django.urls import path
from . import views




urlpatterns = [
    path('ciudades', views.ciudades, name='ciudades'),
    path('categoria_restaurante', views.categoria_restaurante, name='categoria_restaurante'),
    path('login', views.login, name = 'login'),
    path('logout/login', views.login, name = 'login'),
    path('accounts/login/registro', views.registro, name = 'registro'),
    path('', views.home, name = 'home'),
    path('productos', views.productos, name = 'productos'),
    path('logout/', views.exit, name = "exit"),
    path('perfil', views.perfil, name = "perfil"),
    path('accounts/logout/registro', views.registro, name="registro"),
    path('logout/registro', views.registro, name="registro"),
    path('registro', views.registro, name="registro"),
    path('restaurantes', views.restaurantes, name="restaurantes"),
    path('restaurantes/carta', views.carta, name="carta"),
    path('pedido', views.pedido, name="pedido"),


    #path('accounts/', include('django.contrib.auth.urls')),
]
    # path('categorias/<int:ciudad>', views.categoria_restaurante, name='categorias'),
