# 🏴‍☠️ Pirata Market – Sistema de Gestión de Abarrotes

Pirata Market es una aplicación web desarrollada en *Django* para la gestión integral de una cadena de abarrotes.  
Incluye catálogo público de productos, carrito de compras, sistema de pedidos, punto de venta (POS) para empleados, control de inventario y manejo de múltiples sucursales (bodegas).

El sistema está pensado para simular un entorno real de ventas tanto en línea como en tienda física.

---

## 🚀 Funcionalidades principales

### 🛒 Clientes
- Navegación pública del catálogo de productos
- Carrito de compras
- Generación de pedidos
- Pedidos asociados a una sucursal

### 🧑‍💼 Empleados
- Login seguro
- Dashboard administrativo
- Punto de Venta (POS)
- Gestión de inventario por bodega
- Visualización y control de pedidos
- Estados de pedido: pendiente, pagado, preparado, entregado y cancelado

### 📦 Inventario
- Control de stock por presentación
- Stock mínimo
- Ajustes manuales
- Descuento automático de inventario al cobrar pedidos o ventas

---

## 🛠️ Tecnologías utilizadas

- *Backend:* Django 5
- *Base de datos:* PostgreSQL (Supabase)
- *Frontend:* HTML5, CSS3, Django Templates
- *Autenticación:* Django Auth
- *Deploy:* Render
- *Control de versiones:* Git & GitHub

---

## 📊 Diagramas

### Modelo Entidad–Relación Basico
![ER](diagramas/Diagrama_ER_Basico.drawio.png)
