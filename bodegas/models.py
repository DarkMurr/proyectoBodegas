from django.db import models
from catalogo.models import Presentacion

class Bodega(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.TextField()
    telefono = models.CharField(max_length=20, blank=True)
    descripcion = models.TextField(blank=True)
    activa = models.BooleanField(default=True)
    fecha_registro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre

class Inventario(models.Model):

    stock = models.PositiveIntegerField()
    stock_minimo = models.PositiveIntegerField(default=0)
    unidad_stock = models.CharField(max_length=30)
    activo = models.BooleanField(default=True)
    bodega = models.ForeignKey(Bodega, on_delete=models.CASCADE, related_name='inventarios')
    presentacion = models.ForeignKey(Presentacion, on_delete=models.PROTECT, related_name='inventarios')

    class Meta:
        unique_together = ('bodega', 'presentacion')
    def _str_(self):
        return f"{self.presentacion} - {self.bodega}"