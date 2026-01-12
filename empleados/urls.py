from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='empleados_dashboard'),

    # 📦 Inventario
    path('inventario/', views.inventario, name='inventario'),
    path('inventario/ajustar/<int:inventario_id>/', views.ajustar_stock, name='ajustar_stock'),

    # 🧾 POS / Ventas
    path('ventas/', views.pos, name='pos'),
    path('ventas/agregar/<int:presentacion_id>/', views.pos_agregar, name='pos_agregar'),
    path('ventas/quitar/<int:presentacion_id>/', views.pos_quitar, name='pos_quitar'),
    path('ventas/cobrar/', views.pos_cobrar, name='pos_cobrar'),

    # Pedidos
    path('pedidos/', views.pedidos_pendientes, name='pedidos_pendientes'),
    path('pedidos/<int:pedido_id>/', views.pedido_detalle, name='pedido_detalle'),
    path('pedidos/<int:pedido_id>/cobrar/', views.cobrar_pedido, name='cobrar_pedido'),
    path('pedidos/<int:pedido_id>/entregar/', views.entregar_pedido, name='entregar_pedido'),
    path('pedidos/<int:pedido_id>/cancelar/', views.cancelar_pedido, name='cancelar_pedido'),   

    # 📦 Productos
    path('productos/', views.productos, name='productos'),
]
