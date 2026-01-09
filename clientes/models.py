from django.db import models

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100, blank=True)
    correo = models.EmailField(blank=True, null=True)
    telefono = models.CharField(max_length=20, blank=True)
    es_asociado = models.BooleanField(default=False)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    activo = models.BooleanField(default=True)

    def __str__(self):
        tipo = "Asociado" if self.es_asociado else "Visitante"
        return f"{self.nombre} ({tipo})"

