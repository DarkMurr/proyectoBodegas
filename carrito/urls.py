from django.urls import path
from .views import (
    agregar_al_carrito,
    ver_carrito,
    quitar_uno,
    eliminar_del_carrito,
    confirmar_pedido,   
)

urlpatterns = [
    path('', ver_carrito, name='ver_carrito'),
    path('agregar/<int:presentacion_id>/', agregar_al_carrito, name='agregar_carrito'),
    path('quitar/<int:presentacion_id>/', quitar_uno, name='quitar_uno'),
    path('eliminar/<int:presentacion_id>/', eliminar_del_carrito, name='eliminar_carrito'),
    path('confirmar/', confirmar_pedido, name='confirmar_pedido'),  
]