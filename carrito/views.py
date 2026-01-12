from django.shortcuts import render, redirect, get_object_or_404
from decimal import Decimal
from django.http import JsonResponse
from catalogo.models import Presentacion
from pedidos.models import Pedido, DetallePedido
from bodegas.models import Bodega

def agregar_al_carrito(request, presentacion_id):
    carrito = request.session.get('carrito', {})

    presentacion = get_object_or_404(Presentacion, id=presentacion_id)
    pid = str(presentacion.id)

    precio = Decimal(presentacion.precio)

    if pid not in carrito:
        carrito[pid] = {
            'producto': presentacion.producto.nombre,
            'presentacion': f"{presentacion.tamano} {presentacion.unidad_medida}",
            'precio': str(precio),    
            'cantidad': 0,
            'subtotal': "0.00"
        }

    carrito[pid]['cantidad'] += 1

    carrito[pid]['subtotal'] = str(
        Decimal(carrito[pid]['precio']) * carrito[pid]['cantidad']
    )

    request.session['carrito'] = carrito
    request.session.modified = True

    return JsonResponse({'ok': True})


def ver_carrito(request):
    carrito = request.session.get('carrito', {})

    total = Decimal("0.00")

    for item in carrito.values():
        total += Decimal(item['subtotal'])

    return render(request, 'carrito/carrito.html', {
        'carrito': carrito,
        'total': total
    })


def quitar_uno(request, presentacion_id):
    carrito = request.session.get('carrito', {})
    pid = str(presentacion_id)

    if pid in carrito:
        carrito[pid]['cantidad'] -= 1

        if carrito[pid]['cantidad'] <= 0:
            del carrito[pid]
        else:
            carrito[pid]['subtotal'] = str(
                Decimal(carrito[pid]['precio']) * carrito[pid]['cantidad']
            )

    request.session['carrito'] = carrito
    request.session.modified = True

    return JsonResponse({'ok': True})


def eliminar_del_carrito(request, presentacion_id):
    carrito = request.session.get('carrito', {})
    pid = str(presentacion_id)

    if pid in carrito:
        del carrito[pid]

    request.session['carrito'] = carrito
    return redirect('ver_carrito')

def confirmar_pedido(request):
    carrito = request.session.get('carrito', {})
    if not carrito:
        return redirect('ver_carrito')
    bodega = Bodega.objects.first()

    total = 0

    pedido = Pedido.objects.create(
        cliente=None,      
        estado='pendiente',
        total=0,
        bodega=bodega      
    )

    for pid, item in carrito.items():
        presentacion = Presentacion.objects.get(id=pid)
        subtotal = float(item['precio']) * item['cantidad']
        total += subtotal

        DetallePedido.objects.create(
            pedido=pedido,
            presentacion=presentacion,
            cantidad=item['cantidad'],
            precio_unitario=item['precio'],
            subtotal=subtotal
        )

    pedido.total = total
    pedido.save()

    # 🧹 vaciar carrito
    request.session['carrito'] = {}
    request.session['pedido_confirmado'] = True
    request.session.modified = True


    return redirect('catalogo')