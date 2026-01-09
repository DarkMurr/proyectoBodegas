from django.db import models

class Categoria(models.Model):
    nombre = models.CharField(max_length=100, unique = True)
    descripcion = models.TextField(blank=True)

    def __str__(self):
        return self.nombre

class Proveedor(models.Model):
    TIPO_CHOICES = [('marca','Marca'), ('distribuidor','Distribuidor'),('central','Central de Abastos')]
    nombre = models.CharField(max_length=100)
    tipo_proveedor = models.CharField(max_length=20, choices=TIPO_CHOICES)
    telefono = models.CharField(max_length=20, blank=True)
    direccion = models.TextField(blank=True)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre
    
class Producto(models.Model):
    nombre = models.CharField(max_length=150)
    marca = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=150)
    activo = models.BooleanField(default=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT, related_name='productos')

    def __str__(self):
        return f"{self.nombre} -> {self.marca}"

class ProveedorProducto(models.Model):
    precio_compra = models.DecimalField(max_digits=10, decimal_places=2)
    unidad_compra = models.CharField(max_length=20, help_text="Ejemplo: pz, caja, costal, etc.")
    cantidad_compra = models.PositiveIntegerField(help_text="Cantidad comprada en la ultima orden.")
    fecha_compra = models.DateField(null=True, blank=True)
    activo = models.BooleanField(default=True)
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE, related_name='productos_proveidos')
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, related_name='proveedores')

    class Meta:
        unique_together = ('proveedor', 'producto')
    def __str__(self):
        return f"{self.proveedor} -> {self.producto}"

class Presentacion(models.Model):
    tamano = models.DecimalField(max_digits=8, decimal_places=2)
    unidad_medida = models.CharField(max_length=20)
    precio = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    codigo_barras = models.CharField(max_length=50, unique=True, null=True, blank=True)
    activo = models.BooleanField(default=True)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, related_name='presentaciones')

    def __str__(self):
        return f"{self.producto.nombre} - {self.tamano} {self.unidad_medida}"