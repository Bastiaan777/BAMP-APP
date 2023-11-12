from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('ciudades', views.ciudades, name='ciudades'),
    path('categorias', views.categoria_restaurante, name='categorias'),
]