from bodegas.models import Inventario
from django.core.exceptions import ValidationError

def validar_stock(presentacion, bodega, cantidad):
    inventario = Inventario.objects.get(
        presentacion=presentacion,
        bodega=bodega
    )

    if inventario.stock < cantidad:
        raise ValidationError(
            f"Stock insuficiente para {presentacion}"
        )

    return inventario


def descontar_stock(presentacion, bodega, cantidad):
    inventario = validar_stock(presentacion, bodega, cantidad)
    inventario.stock -= cantidad
    inventario.save()