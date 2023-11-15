from django.urls import path
from . import views

urlpatterns = [
    path('ciudades', views.ciudades, name='ciudades'),
    path('categorias', views.categoria_restaurante, name='categorias'),
]
    # path('categorias/<int:ciudad>', views.categoria_restaurante, name='categorias'),
