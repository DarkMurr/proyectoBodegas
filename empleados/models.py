from django.db import models
from bodegas.models import Bodega
from django.contrib.auth.models import User

class Empleado(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    correo = models.EmailField(unique=True,help_text="Correo personal del empleado")
    telefono = models.CharField(max_length=20, blank=True)
    puesto = models.CharField(max_length=50, help_text="Puesto general del empleado (Cajero, Administrador, Auxiliar, etc.)")
    activo = models.BooleanField(default=True)
    bodega = models.ForeignKey( Bodega, on_delete=models.PROTECT, related_name='empleados')
    user = models.OneToOneField( User, on_delete=models.CASCADE, help_text="Usuario del sistema")

    def __str__(self):
        return f"{self.nombre} {self.puesto}"
    
class Administrador(models.Model):
    empleado = models.OneToOneField( Empleado, on_delete=models.CASCADE, primary_key=True)
    nivel_acceso = models.PositiveSmallIntegerField(default=1)

    def __str__(self):
        return f"Admin: {self.empleado.nombre}"


class Cajero(models.Model):
    empleado = models.OneToOneField(Empleado, on_delete=models.CASCADE, primary_key=True)
    turno = models.CharField(max_length=20)

    def __str__(self):
        return f"Cajero: {self.empleado.nombre}"

class Auxiliar(models.Model):
    empleado = models.OneToOneField(Empleado, on_delete=models.CASCADE, primary_key=True)
    area = models.CharField(max_length=50)

    def __str__(self):
        return f"Auxiliar: {self.empleado.nombre}"
