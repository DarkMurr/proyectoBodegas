from django.db import models
from empleados.models import Cajero
from clientes.models import Cliente
from pagos.models import Pago
from catalogo.models import Presentacion

class Ticket(models.Model):
    fecha = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    pago = models.OneToOneField(Pago, on_delete=models.SET_NULL, null=True, blank=True)
    cajero = models.ForeignKey(Cajero, on_delete=models.PROTECT,related_name='tickets')
    cliente = models.ForeignKey(Cliente, on_delete=models.SET_NULL, null=True, blank=True, help_text="Cliente asociado si existe, puede ser null para venta anónima")
    def __str__(self):
        return f"Ticket #{self.id} - ${self.total}"


class DetalleTicket(models.Model):
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE, related_name='detalles')
    presentacion = models.ForeignKey(Presentacion, on_delete=models.PROTECT)
    cantidad = models.PositiveIntegerField()
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.presentacion} x {self.cantidad}"