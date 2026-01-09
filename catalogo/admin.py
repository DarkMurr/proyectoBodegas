from django.contrib import admin
from .models import (
    Categoria,
    Proveedor,
    Producto,
    Presentacion,
    ProveedorProducto
)

admin.site.register(Categoria)
admin.site.register(Proveedor)
admin.site.register(Producto)
admin.site.register(Presentacion)
admin.site.register(ProveedorProducto)

