from django.urls import path
from . import views




urlpatterns = [
    path('ciudades', views.ciudades, name='ciudades'),
    path('categoria_restaurante', views.categoria_restaurante, name='categoria_restaurante'),
    path('login', views.login, name = 'login'),
    path('home', views.home, name = 'home'),
    path('productos', views.productos, name = 'productos'),
    path('logout/', views.exit, name = "exit"),
    #path('accounts/', include('django.contrib.auth.urls')),
]
    # path('categorias/<int:ciudad>', views.categoria_restaurante, name='categorias'),
