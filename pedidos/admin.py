from django.contrib import admin
from .models import Pedido, DetallePedido

class DetallePedidoInline(admin.TabularInline):
    model = DetallePedido
    extra = 1

@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ('id', 'fecha', 'cliente', 'estado', 'total', 'bodega')
    list_filter = ('estado', 'bodega')
    inlines = [DetallePedidoInline]
