from django.db import models

class Pago(models.Model):

    METODO_CHOICES = [
        ('efectivo', 'Efectivo'),
        ('tarjeta', 'Tarjeta'),
        ('transferencia', 'Transferencia'),
    ]

    ESTADO_CHOICES = [
        ('pendiente', 'Pendiente'),
        ('confirmado', 'Confirmado'),
        ('cancelado', 'Cancelado'),
    ]

    fecha = models.DateTimeField(auto_now_add=True)
    metodo = models.CharField(max_length=20, choices=METODO_CHOICES)
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='pendiente')
    referencia = models.CharField(max_length=100, blank=True,help_text="Referencia bancaria, folio o identificador de pago")

    def _str_(self):
        return f"{self.metodo} - ${self.monto} ({self.estado})"
