import django_filters

from .models import Producto

class ProductoFilter(django_filters.FilterSet):
    class Meta:
        model = Producto
        fields = {
            'restaurante__categoria': ['exact'],
        }