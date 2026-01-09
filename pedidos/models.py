from django.db import models
from clientes.models import Cliente
from pagos.models import Pago
from catalogo.models import Presentacion
from bodegas.models import Bodega


class Pedido(models.Model):
    ESTADO_CHOICES = [
        ('pendiente', 'Pendiente'),
        ('pagado', 'Pagado'),
        ('preparado', 'Preparado'),
        ('entregado', 'Entregado'),
        ('cancelado', 'Cancelado'),
    ]

    fecha = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES,default='pendiente')
    cliente = models.ForeignKey(Cliente, on_delete=models.SET_NULL, null=True, blank=True, help_text="Cliente que realiza el pedido (puede ser visitante)")
    bodega = models.ForeignKey(Bodega, on_delete=models.PROTECT, related_name='pedidos', help_text="Bodega donde se recogerá el pedido")
    pago = models.OneToOneField(Pago, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"Pedido #{self.id} - {self.estado} - ${self.total}"
    
class DetallePedido(models.Model):
    cantidad = models.PositiveIntegerField()
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE, related_name='detalles')
    presentacion = models.ForeignKey(Presentacion, on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.presentacion} x {self.cantidad}"